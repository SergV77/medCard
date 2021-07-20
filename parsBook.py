from settingMedCard import *
from functionMedCard import *
import fitz
from PyPDF2 import PdfFileReader
import pdfminer

import io
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from pdfminer.layout import LAParams



# path = 'db/book/biliary tract.pdf'
path = 'db/book/Liver_biliary tract_pancreas.pdf'
path2 = 'db/book/Liver_biliary tract_pancreas.txt'


#
doc = fitz.open(path)
book_list = []
for current_page in range(34, 182):
    page_text = []
    page = doc.loadPage(current_page)
    page_text = page.get_text('text')
    book_list.append(page_text.split(" "))


# print(book_list)
for line in book_list:
    for word in line:
        if word == 'Глава':
            print(word)
#
# regex_num1 = re.compile(r'Глава \d')
# regex_num2 = re.compile(r'(\d\.\d\.\s[А-Я]\w+)\n')
# regex_num3 = re.compile(r'(\d\.\d\.\d\. [А-Я]\w+\s\w+)')
# regex_num4 = re.compile(r'[А-Я]\w+')
#
# # for i, el in enumerate(book_list):
# #     print(i, ' - ', type(el))
# # #
# find_words = ['Жалобы', 'Анамнез']
#
# book_dict = {}
# for i, el in enumerate(book_list):
#     # print(i, '0 - ', el.replace('\n', ' '))
#     if len(regex_num1.findall(el)) != 0:
#         # print(i, '1 - ', regex_num1.findall(el)[0])
#         if regex_num1.findall(el)[0] not in book_dict.keys():
#             book_dict[regex_num1.findall(el)[0]] = el
#         else:
#             book_dict[regex_num1.findall(el)[0]] += el
#     # print(i, '2 - ', regex_num2.findall(el))
#     # print(i, '3 - ', regex_num3.findall(el))
#     # print(i, '4 - ', regex_num4.findall(el))
#
# for k, v in book_dict.items():
#     print(k, ' - ', v)
#





#
# for i, el in enumerate(book_list):
#     # print(i, '0 - ', el.replace('\n', ' '))
#     if len(regex_num1.findall(el)) != 0:
#         # print(i, '1 - ', regex_num1.findall(el)[0])
#         if regex_num1.findall(el)[0] not in book_dict.keys():
#             book_dict[regex_num1.findall(el)[0]] = el
#         else:
#             book_dict[regex_num1.findall(el)[0]] += el
#     # print(i, '2 - ', regex_num2.findall(el))
#     # print(i, '3 - ', regex_num3.findall(el))
#     # print(i, '4 - ', regex_num4.findall(el))
#
# for k, v in book_dict.items():
#     print(k, ' - ', v)

#
# for el in book_list:
#    print(el)
# #
# regex_num = re.compile(r'(\d+\.\d+\.)\s*([А-Я]\w+)\s([а-я]\w+)\n')
# for el in book_list[10]:
#     print(el)
#     for i in el:
#         if len(regex_num.findall(i)) != 0:
#             print(regex_num.findall(i))
#









# print(book_list)
#
# search_term = "Клиническая картина"
# pdf_document = fitz.open(path)
# for current_page in range(len(pdf_document)):
#     page = pdf_document.loadPage(current_page)
#     if page.searchFor(search_term):
#         print("%s найдено на странице %i" % (search_term, current_page+1))

# pdf_file = fitz.open(path)
# print("number of pages: %i" % pdf_file.pageCount)
# print(pdf_file.metadata)
#
# dis_book = []
# for i in range(pdf_file.pageCount):
#     page = []
#     page = pdf_file.loadPage(i)
#     pageText = page.getText("text")
#     print(page)
#     pageText = pageText.extractText()
#     print(pageText)
#
#
#
#     dis_book.append(pageText)


# regex = r"^\d+(?:\.\d+)* .*(?:\r?\n(?!\d+(?:\.\d+)* ).*)*"
# print(re.findall(regex,samplestring, re.M))
#


# print(len(dis_book))
#
# new_dis_book = []
# for el in dis_book:
#     el = el.replace('\n', '')
#     new_dis_book.append(el)
#     print(el.split('.'))


# search_term = "invoice"
# pdf_document = fitz.open(path)
#
# for current_page in range(len(pdf_document)):
#    page = pdf_document.loadPage(current_page)
#    if page.searchFor(search_term):
#        print("%s found on page %i" % (search_term, current_page))
#
# #
# for el in new_dis_book:
#     for word in el.split(' '):
#         if word.isupper() and len(word) > 4:
#             print(word)

#


# dis_book.append(page.getText("text"))






    # for k, v in doc.items():
    #     if k == 'Диагноз' or k == 'Жалобы' or k == 'Статус при поступлении' or k == 'Анамнез болезни':
    #         for junk_char in "%$\\>//<+=@*-?!& \n":
    #             v = ''.join(v).replace(junk_char, ' ')
    #             v = ''.join(v).replace(' ', ' ')
    #         new_dict[k] = v
    #
    #


#
# with open(path, "rb") as filehandle:
#     pdf = PdfFileReader(filehandle)
#     info = pdf.getDocumentInfo()
#     pages = pdf.getNumPages()
#     print(info)
#     print("number of pages: %i" % pages)
#
#     page1 = pdf.getPage(22)
#     print(page1)
#     print(page1.extractText())

#
# #
#
# search_term = "invoice"
# pdf_document = fitz.open(path)
#
# for current_page in range(len(pdf_document)):
#     page = pdf_document.loadPage(current_page)
#     if page.searchFor(search_term):
#         print("%s found on page %i" % (search_term, current_page))
#
# for current_page in range(len(pdf_document)):
#     for image in pdf_document.getPageImageList(current_page):
#         xref = image[0]
#         pix = fitz.Pixmap(pdf_document, xref)
#         if pix.n < 5:        # this is GRAY or RGB
#             pix.writePNG("page%s-%s.png" % (current_page, xref))
#         else:                # CMYK: convert to RGB first
#             pix1 = fitz.Pixmap(fitz.csRGB, pix)
#             pix1.writePNG("page%s-%s.png" % (current_page, xref))
#             pix1 = None
#         pix = None
#
# for i in range(pdf_file.pageCount):
#     page = []
#     page = pdf_file.loadPage(i)
#     dl = page.getDisplayList()
#     tp = dl.getTextPage()
#     tp_text = tp.extractText()
#     print(re.split('\n\d+.+[ \t][а-яА-Я].+\n', tp_text))
#     # print(re.split('\n\d+.+[ \t][[а-яА-Я].+\n', "some text\n1. heading 1\nparagraph 1\n1.2.3 Heading 2\nparapgraph 2"))
#     dis_book.append(tp_text)
#
# print(len(dis_book))

# !/usr/bin/python
#
# import fitz
#
# pdf_document = "example.pdf"
# doc = fitz.open(pdf_document):
# print("number of pages: %i" % doc.pageCount)
#
# print(doc.metadata)
# page1 = doc.loadPage(0)
# page1text = page1.getText("text")
# print(page1text)


# pdf_reader = PdfFileReader(path)
# output_file_path = path2
#
# with open(path2, mode="w", encoding='utf-8') as output_file:
#     title = pdf_reader.documentInfo.title
#     num_pages = pdf_reader.getNumPages()
#     output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")
#     for page in pdf_reader.pages:
#         text = page.extractText()
#         output_file.write(text)
#
# doc = fitz.open(path)
# print("Исходный документ: ", doc)
# print("\nКоличество страниц: %i\n\n------------------\n\n" % doc.pageCount)
# print(doc.metadata)
#
# book_list = []
# for current_page in range(36, 37):
#     page_text = []
#     page = doc.loadPage(current_page)
#     page_text = page.get_text('text')
#     print(page_text)
#
#     #print("Стр. ", current_page+1, "\n\nСодержание;\n")
#     # print('1 - ', re.split('\n\d+.+[ \t][а-яА-Я].+\n', page_text))
#     # book_list.append(re.split('\n\d+.+[ \t][а-яА-Я].+\n', page_text))
#     book_list.append(page_text)
#     print('2 - ', re.split('\n\d+.\d+.+[\t][а-яА-Я].+\n', page_text))
#     print('3 - ', re.split('\n\d+ . \d+ . \d+ . +[\t][а-яА-Я]. + \n', page_text))
#     print(page_text)
# new_book_list = []
# for el in book_list:
#     new_book_list.append(el[0].split(' '))
#
#
#
#
#
# regex_num = re.compile(r'(\d\.\d\.\d\.)\s([А-Я]\w+)')
# regex_num1 = re.compile(r'Глава \d\n')
# regex_num2 = re.compile(r'(\d\.\d\.\s[А-Я]\w+)\n')
# regex_num3 = re.compile(r'Жалоба\n')
#
# # for i, el in enumerate(book_list):
# #     print(i, ' - ', type(el))
# # #
# for i, el in enumerate(book_list):
#     print(i, '1 - ', el.replace('\n', ' '))
#     print(i, '2 - ', regex_num1.findall(el))
#     print(i, '3 - ', regex_num2.findall(el))
#     print(i, '4 - ', regex_num3.findall(el))
# #
# for el in book_list:
#    print(el)
# #
# regex_num = re.compile(r'(\d+\.\d+\.)\s*([А-Я]\w+)\s([а-я]\w+)\n')
# for el in book_list[10]:
#     print(el)
#     for i in el:
#         if len(regex_num.findall(i)) != 0:
#             print(regex_num.findall(i))
#



