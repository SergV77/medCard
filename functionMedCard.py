from settingMedCard import *

#Поиск необходимых файлов
def findDoc():
    paths = []
    folder = os.getcwd()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('docx') and not file.startswith('~'):
                paths.append(os.path.join(root, file))
    return paths

#Открытие файлов pdf
def openPdf(path):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages
        card1 = []
        for i in range(len(page)):
            card1.append(pdf.pages[i].extract_text())

#Парссинг таблиц
def parsDoctable(table):
    tab_list = []
    for tab in table.tables:
        for row in tab.rows:
            temp_tab = []
            for cell in row.cells:
                temp_tab.append(cell.text)
            if len(temp_tab) > 3:
                tab_list.append(temp_tab)
    return tab_list

#Парссинг текста
def parsDocText(doc):
    doc_list = []
    tab_list = []
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                doc_list.append(cell.text)
                tab_list += parsDoctable(cell)
    return doc_list, tab_list

def getText(doc_file):
    text = []
    for paragraph in doc_file.paragraphs:
        text += paragraph.text.split('\n')
        # '\n'.join(paragraph.text)
    if text != [""]:
        return text


#Открытие файлов doc
def openDoc(path):
    text = []
    table = []
    doc_file = docx.Document(path)
    text = getText(doc_file)
    if text != None:
        return text, table
    else:
        text, table = parsDocText(doc_file)
        return text, table

#Удаляем не нужные символы
def clean_word(item):
    for p in string.punctuation:
        if p in item:
            item = item.replace(p, '')
            item = item.replace('\xa0', ' ')
    return item.strip()

def getDict(doc_list):
    dict_list = {}

    for item in doc_list:
        if len(item) != '':
            key = item.split(":")[0]
            value = item.split(":")[1:]
            if key != '':
                dict_list[key] = value
    if dict_list != 0:
        return dict_list


def madeDictData(doc_list):
    if type(doc_list) != list:
        return getDict(doc_list[0])

    return getDict(doc_list)

# def madeListData(doc_list):
#     new_dict = {}
#
#     dict_list = madeDictData(doc_list)
#     for k, v in dict_list.items():
#         #print(k, ' - ', v)
#         if k == 'Диагноз' or k == 'Жалобы' or k == 'Статус при поступлении' or k == 'Анамнез болезни':
#             for junk_char in "%$\\>//<+=@*-?!& \n":
#                 v = ''.join(v).replace(junk_char, ' ')
#                 v = ''.join(v).replace(' ', ' ')
#
#     return dict_list

#Открытие файлов doc
# def openDoc(path):
#     text = []
#     table = []
#     doc_file = docx.Document(path)
#     text, table = parsDocText(doc_file)
#
#     # if len(table) != 0:
#     return text, table