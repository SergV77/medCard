from settingMedCard import *
from functionMedCard import *
from compoundfiles import CompoundFileReader, CompoundFileError
from struct import unpack

# doc = docx.Document('51.docx')
#
#
#
#


paths = findDoc()
print(paths)
print(len(paths))


data = []
big_table = []
for path in paths:

    doc, table = openDoc(path)
    doc = madeDictData(doc)
    big_table.append((path.split('\\')[-1].split('.')[0], table))
    #data.append(doc)

    new_dict = {}
    for k, v in doc.items():
        if k == 'Диагноз' or k == 'Жалобы' or k == 'Статус при поступлении' or k == 'Анамнез болезни':
            for junk_char in "%$\\>//<+=@*-?!& \n":
                v = ''.join(v).replace(junk_char, ' ')
                v = ''.join(v).replace(' ', ' ')
            new_dict[k] = v

    if len(new_dict) > 0:
        data.append((path.split('\\')[-1].split('.')[0], new_dict))

# for el in data:
#     print(el)
# print(len(data))



dis = []
sym = []
for ind, val in enumerate(data):
    for key, value in val[1].items():
        if key == 'Диагноз':
            dis.append((ind, val[0], value))
        else:
            sym.append((ind, val[0], key, value))

dis_kod = []
dis_name = []
all_dis = []
for el in dis:
    dis_kod.append((el[0], el[1], el[2].split(',')[1:][0].split(' ')[2:][0]))
    dis_name.append((el[0], el[1], ' '.join(el[2].split(',')[1:][0].split(' ')[2:][1:])))
    all_dis.append([el[0], el[1], el[2].split(',')[1:][0].split(' ')[2:][0], ' '.join(el[2].split(',')[1:][0].split(' ')[2:][1:])])

symptoms = {}
for num, el in enumerate(sym):
    print(el)
    if el[0] not in symptoms.keys():
        symptoms[el[0]] = [(el[1], clean_word(el[3]))]
    else:
        symptoms[el[0]].append((el[1], clean_word(el[3])))

for k, v in symptoms.items():
    print(k, ' - ', v)



print(len(data))

# fieldnames = ['class', 'num_diagnosis', 'name_diagnosis']
# with open('db/epicrisis/outer/yTrain.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(fieldnames)
#     for el in all_dis:
#         file_writer.writerow(el)

#
# fieldnames = ['class', 'name_symptoms']
# with open('db/epicrisis/outer/xTrain2.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(fieldnames)
#     for k, v in symptoms.items():
#         file_writer.writerow([k, (*v)])
#
# fieldnames = ['class', 'table_symptoms']
# with open('db/epicrisis/outer/xTrain3.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(fieldnames)
#     for k, v in symptoms.items():
#         file_writer.writerow([k, (*v)])

# for item in doc_list:
#     if len(item) != 0:
#         key = item.split(":")[0]
#         value = item.split(":")[1:]
#         dict[key] = value
# print(dict)
#
# for k, v in dict.items():
#     #print(k, ' - ', v)
#     if k == 'Диагноз' or k == 'Жалобы' or k == 'Статус при поступлении' or k == 'Анамнез болезни':
#         for junk_char in "%$\\>//<+=@*-?!& \n":
#             v = ''.join(v).replace(junk_char, ' ')
#             v = ''.join(v).replace(' ', ' ')
#
#         print(k, ' - ', v)


#
# for table in doc.tables:
#     for row in table.rows:
#         for cell in row.cells:
#             doc_list.append(cell.text)
#             #print(cell.text)
#             for tab in cell.tables:
#                 for row in tab.rows:
#                     for cell in row.cells:
#                         tab_list.append(cell.text)
#
#
# for item in doclist2:
#     print(item)
#
# bad_chars = ["*", " ", '+', '//', '\\', '@', '#', '$', '%', '^', '&', '(', ')', '{', '}', '[', ']', '|', '<', '>', '\n', '?']
#
#
# card = {}
# doc_list = []
# docTable = []
# dict = dict()
# th = ['Наименование', '04.03.2021 14:00', 'Единицы', 'Границы норм']
# tab_list = []
# columns = len(th)  # Подсчитаем кол-во столбцов на будущее.
# new_table = PrettyTable(th)  # Определяем таблицу.
#
# #
# is_kod = []
# dis_name = []
# all_dis = []
# for el in dis:
#     dis_kod.append((el[0], el[4].split(',')[4:][0].split(' ')[2:][0]))
#     dis_name.append((el[0], ' '.join(el[1].split(',')[1:][0].split(' ')[2:][1:])))
#     all_dis.append([el[0], el[1].split(',')[1:][0].split(' ')[2:][0], ' '.join(el[1].split(',')[1:][0].split(' ')[2:][1:])])
#
# symptoms = {}
# for num, el in enumerate(sym):
#     print(el)
#     if el[0] not in symptoms.keys():
#         symptoms[el[0]] = [clean_word(el[2])]
#     else:
#         symptoms[el[0]].append(clean_word(el[2]))
#
# for k, v in symptoms.items():
#     print(k, ' - ', v)

#
# for table in doc.tables:
#     for row in table.rows:
#         for cell in row.cells:
#             print(cell.text)
#
# #card['Диагноз'] = ''.join(v).replace(' ', ' ')
# # for table in doc.tables:
# #     for row in table.rows:
# #         for cell in row.cells:
# #             print(cell.text)
# #
# for table in doc.tables:
#     for index, row in enumerate(table.rows):
#         if index == 0:
#             row_text = list(cell.text for cell in row.cells)
#             if 'Наименование' not in row_text:
#                 break
#         for cell in row.cells:
#             print(cell.text)
#
# new_text = []
# for el in doclist:
#     if el != '':
#         if el not in new_text:
#             new_text.append(el)
#
# # print(new_text)
#
# for el in new_text:
#     print(el.split('\n'))

# bad_chars = ["*", " ", '+', '//', '\\', '@', '#', '$', '%', '^', '&', '(', ')', '{', '}', '[', ']', '|', '<', '>', '\n', '?']
# new_td = [el for el in td if el not in bad_chars ]
# while new_td:
#     new_table.add_row(new_td[:columns])
#     new_td = new_td[columns:-24]
# print(len(new_td))
# print(new_td)
# print(new_table)  # Печатаем таблицуS


#
#
#
#print(new_table)  # Печатаем таблицу

#
# th = ['MAC Address', 'IP Address', 'Mode', 'Rate (Mbps)', 'Signal (%)']
# td = ['11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
#       '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
#       '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
#       '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
#       '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100']
#



