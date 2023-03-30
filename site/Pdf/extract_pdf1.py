import PyPDF2
a = PyPDF2.PdfFileReader('roller-chain-sprockets.pdf')
#print(a.documentInfo)
#print(a.getNumPages())
str = ""
for i in range(12, 13):
    str += a.getPage(i).extractText()
with open('roller-chain-sprockets1.txt', 'w', encoding='utf-8') as f:
    f.write(str)