#Metadata ectraction in python

#Author creator producer subject title no.of.pages
#pdf miner
from PyPDF2 import PdfFileReader, PdfFileWriter
def extractInfo(pdfPath):
    with open(pdfPath,'rb') as file:
        pdf=PdfFileReader(file)
        information=pdf.getDocumentInfo()
        totalPages=pdf.getNumPages()
    txt = f"""
    Information about {pdf}
    Author : {information.author}
    Creator : {information.creator}
    Subject : {information.subject}
    Title : {information.title}


    """
    print(txt)
#merging pdf

#systems@nayatel.com
def merge_pdfs(paths,output):
    pdf_writer=PdfFileWriter()
    for path in paths:
        pdf_reader=PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__=='__main__':
    # path='UsmanKhalid_CV.pdf'
    # extractInfo(path)
    input=['cv.pdf','cv2.pdf']
    merge_pdfs(input,output='merge.pdf')