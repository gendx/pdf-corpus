class PDFDictionary:
    def __init__(self, d):
        self.dictionary = d

    def __str__(self):
        result = ""
        for k, v in self.dictionary.items():
            if len(result) > 0:
                result += " "
            result += "/" + k + " " + v
        return "<<" + result + ">>"

class PDFObject:
    def __init__(self, content, numgen):
        self.content = content
        self.num, self.gen = numgen

    def __str__(self):
        return str(self.num) + " " + str(self.gen) + " obj" + "\n" + self.content + "\nendobj\n"

class PDFStream:
    def __init__(self, dictionary, content, numgen):
        dictionary["Length"] = str(len(content))
        d = PDFDictionary(dictionary)
        self.pdfobject = PDFObject(str(d) + "\nstream\n" + content + "\nendstream", numgen)

    def __str__(self):
        return str(self.pdfobject)

