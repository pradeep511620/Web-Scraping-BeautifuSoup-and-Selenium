# importing required modules
import PyPDF2

# creating a pdf file object
# pdfFileObj = open(r'C:/Users/nextgenraptor/Downloads/Tutorial_Python.pdf', 'rb')
pdfFileObj = open(r'roller-chain-sprockets.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()