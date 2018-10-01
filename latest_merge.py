#!/usr/bin/env python
from pdfrw import PdfReader, PdfWriter, PageMerge
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

def get4(srcpages):

    scale = 1/len(pages)
    srcpages = PageMerge() + srcpages
    x_increment, y_increment = (scale * i for i in srcpages.xobj_box[2:])
    for i, page in enumerate(srcpages):
        page.scale(scale)
        page.x = x_increment if i & 2 else 1
        page.y = 0 if i & 1 else y_increment

    return srcpages.render()


pages = PdfReader('document-output.pdf').pages
writer = PdfWriter('out.pdf')

for index in range(0, len(pages), len(pages)):
    print(len(pages))
    writer.addpage(get4(pages[index:index + len(pages)]))

writer.write()

reader = PdfFileReader(open("out.pdf",'rb'))
invoice_page = reader.getPage(0)
sup_reader = PdfFileReader(open("download.pdf",'rb'))
sup_page = sup_reader.getPage(0)  # We pick the second page here

translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight())
translated_page.mergeScaledTranslatedPage(sup_page, 1, 0, 0)  # -400 is approximate mid-page

translated_page.mergePage(invoice_page)

writer = PdfFileWriter()
writer.addPage(translated_page)

with open('output1.pdf', 'wb') as f:
    writer.write(f)