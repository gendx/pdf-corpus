from pdfobject import PDFObject

class PDFFile:
    def __init__(self, objects):
        self.objects = objects

    def save(self, filename):
        with open(filename, 'w') as out:
            # header
            size = self.write_header(out)
            # objects
            offsets, size = self.write_objects(out, size)
            # xref table
            count = self.write_xref(out, offsets)
            # trailer
            self.write_trailer(out, count, size)

    def write_header(self, out):
        header = '%PDF-1.7\n%\x80\x80\x80\x80\n'
        size = len(header)
        out.write(header)
        return size

    def write_objects(self, out, size):
        offsets = {}
        for numgen in sorted(self.objects.keys()):
            o = self.objects[numgen]
            content = str(o)
            out.write(content)
            offsets[numgen] = size
            size += len(content)
        return offsets, size

    def write_xref(self, out, offsets):
        count = len(offsets)
        out.write('xref\n')
        out.write('0 ' + str(count + 1) + '\n')
        out.write(''.zfill(10) + ' 65535 f \n')
        for numgen in sorted(offsets.keys()):
            num, gen = numgen
            out.write(str(offsets[numgen]).zfill(10) + ' ' + str(gen).zfill(5) + ' n \n')
        return count

    def write_trailer(self, out, count, size):
        out.write('trailer\n<<\n\t/Size ' + str(count + 1) + '\n\t/Root 1 0 R\n')
        out.write('>>\nstartxref\n' + str(size) + '\n%%EOF')

