from pdfobject import PDFObject, PDFStream
from pdffile import PDFFile

class ContentStream:
    def __init__(self, content):
        objects = {}
        objects[(1, 0)] = PDFObject("<< /Type /Catalog /Pages 2 0 R >>", (1, 0))
        objects[(2, 0)] = PDFObject("<< /Type /Pages /Count 1 /Kids [3 0 R] >>", (2, 0))
        objects[(3, 0)] = PDFObject("<< /Type /Page /Resources << /Font << /F1 4 0 R >> >> /MediaBox [0 0 595 842] /Parent 2 0 R /Contents 5 0 R >>", (3, 0))
        objects[(4, 0)] = PDFObject("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Name /F1 >>", (4, 0))
        stm = PDFStream({}, content, (5, 0))
        objects[(5, 0)] = stm.pdfobject
        self.pdffile = PDFFile(objects)

