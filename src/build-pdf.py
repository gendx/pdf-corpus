#!/usr/bin/env python

import sys
import re
from contentstream import ContentStream
from pdfobject import *
from pdffile import PDFFile

def flush_obj(objects, content, objnum, is_stream):
    if objnum is None:
        return

    if is_stream:
        objects[objnum] = PDFStream({}, content, objnum)
    else:
        objects[objnum] = PDFObject(content, objnum)


def convert(src, dst):
    CONTENT_STREAM = 1
    OBJECTS = 2
    typ = None

    regex_objnum = re.compile(r'^--- ([0-9]+) ([0-9]+)$')
    regex_stream = re.compile(r'^--- ([0-9]+) ([0-9]+) stream$')

    parameters = {}

    with open(src, 'r') as fin:
        for i, line in enumerate(fin):
            if typ == None:
                line = line.strip()

                # End of header
                if line[:3] == '---':
                    if 'template' not in parameters:
                        raise Exception('No template declared, aborting.')
                    template = parameters['template']

                    if template == 'contentstream':
                        typ = CONTENT_STREAM
                        content = ''
                    elif template == 'objects':
                        typ = OBJECTS
                        objects = {}
                        content = None
                        objnum = None
                        is_stream = None
                    else:
                        raise Exception('Unknown template "' + template + '", aborting.')
                # Parse header
                else:
                    pos = line.find('=')
                    if pos == -1:
                        raise Exception('Expected parameter (key=value) at line ' + str(i+1) + ', aborting.')

                    key = line[:pos].strip()
                    if len(key) == 0:
                        raise Exception('Expected non-empty key at line ' + str(i+1) + ', aborting.')
                    if key in parameters:
                        raise Exception('Redefinition of parameter "' + key + '" at line ' + str(i+1) + ', aborting.')

                    value = line[(pos+1):].strip()
                    if len(value) == 0:
                        raise Exception('Expected non-empty value at line ' + str(i+1) + ', aborting.')

                    parameters[key] = value

            # Content stream template
            elif typ == CONTENT_STREAM:
                content += line
            # Objects template
            elif typ == OBJECTS:
                m1 = regex_objnum.match(line.rstrip())
                m2 = regex_stream.match(line.rstrip())

                if m1:
                    flush_obj(objects, content, objnum, is_stream)
                    content = ''
                    objnum = (m1.group(1), m1.group(2))
                    is_stream = False
                elif m2:
                    flush_obj(objects, content, objnum, is_stream)
                    content = ''
                    objnum = (m2.group(1), m2.group(2))
                    is_stream = True
                else:
                    if objnum is None:
                        raise Exception('No object declared at line ' + str(i+1) + ', aborting.')
                    content += line

    # Assemble the file
    # Content stream template
    if typ is None:
        raise Exception('Expected end-of-header line "---", aborting.')
    elif typ == CONTENT_STREAM:
        tmp = ContentStream(content)
        tmp.pdffile.save(dst)
    elif typ == OBJECTS:
        flush_obj(objects, content, objnum, is_stream)
        tmp = PDFFile(objects)
        tmp.save(dst)
    else:
        raise Exception('Unknown template, aborting.')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Error: expected two arguments (input and output file names)"
    else:
        convert(sys.argv[1], sys.argv[2])

