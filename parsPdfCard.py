

pdf_document = "Хронический тонзиллит.pdf"


with pdfplumber.open(pdf_document) as pdf:
    page = pdf.pages
    card1 = []
    for i in range(len(page)):
        card1.append(pdf.pages[i].extract_text())

    table = []
    text = []
    for i in range(len(page)):
        page = pdf.pages[i]
        tbl = page.extract_table()
        txt = page.extract_text()
        if tbl != None:
            table.append(tbl)
        text.append(txt)


text = text[0].split('\n')
for line in text:
    if text.index(line) > text.index('Диагноз при выписке') and text.index(line) < text.index('Жалобы'):
        print(line)
    if text.index(line) > text.index('Жалобы') and text.index(line) < text.index('Анамнез заболевания'):
        print(line)
    if text.index(line) > text.index('Анамнез заболевания') and text.index(line) < text.index('Анамнез жизни'):
        print(line)




# for i in range(len(text)):
#     if text[i] == 'Диагноз при поступлении':
#         print(text[i+1])
#         print(text[i + 2])
#         print(text[i + 3])


#
# patterns = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+"
# stopwords_ru = stopwords.words("russian")
# morph = MorphAnalyzer()
#
#
# def lemmatize(doc):
#     doc = re.sub(patterns, ' ', doc)
#     tokens = []
#     for token in doc.split():
#         if token and token not in stopwords_ru:
#             token = token.strip()
#             token = morph.normal_forms(token)[0]
#
#             tokens.append(token)
#     if len(tokens) > 2:
#         return tokens
#     return None
#
# data = lemmatize(text[0])
#
# print(Counter(data))

#
# for tabl in table:
#     for line in tabl:
#         print(line)

# temp_dict = {'Диагноз': [], 'Жалобы': [], 'Анамнез': [], 'Объективный': []}
# print(text[0].split())
# print(len(text))




# for i in range(len(text)):
#    print(text[i].split())



# print('~'*150)
# for el in table1:
#     print(el)
# print('~'*150)
# for el in table2:
#     print(el)