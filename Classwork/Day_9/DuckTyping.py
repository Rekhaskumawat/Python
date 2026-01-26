
# Duck typing : it is concept where the type of an object is determined 
# by its behaviour , not by its class

class InkjetPrinter:

    def PrintDocument(self ,document):
        print("Inkjet printer printing :",document)

class LaserPrinter:

    def PrintDocument(self ,document):
        print("Leaser printer printing :",document)

class PDFWriter:

    def PrintDocument(self ,document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()