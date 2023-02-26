import PyPDF2
import sys

#collects files from aguments in command line
inputs = sys.argv[1:]

#Function to combine files
def pdfCombiner(pdfList):
    merger = PyPDF2.PdfMerger()

    for pdf in pdfList:
        merger.append(pdf)
    merger.write("super.pdf")

pdfCombiner(inputs)

#Add watermarks in combined document
template = PyPDF2.PdfReader(open("super.pdf","rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf","rb"))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open("watermarked.pdf","wb") as file:
        output.write(file)


#create a cloned rotated page
# with open("dummy.pdf", 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.pages[0]
#     page.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)

#     with open("tilt.pdf","wb") as newFile:
#         writer.write(newFile)

