#1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость)
#название файла avto.txt

#2)Создать doc шаблон, где будут использованы данные параметры.
# Название шаблона Shablon.docx


from docxtpl import DocxTemplate
import csv
import json
import time

# 3)Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).+ замер времени
Mylist = []
with open('avto.txt') as file:
    reader = csv.DictReader(file, delimiter = ';')
    for row in reader:
        Mylist.append(row)
print(Mylist)
for i in Mylist:
    start_time = time.time()
    Fname = ''
    for key,values in i.items():
        if key == 'Brend':
            Fname = values
        if key == 'Model':
            Fname = Fname + ' ' + values + '.docx'
    Mydoc = DocxTemplate('Shablon.docx')
    Mydoc.render(i)
    Mydoc.save(Fname)
    print('Документ', Fname, 'формировался', time.time() - start_time, 'сек.')
#4)Создать csv файл с данными о машине.------------------------

fieldnames = ['Brend', 'Model', 'Fuel_consumption', 'Price']
with open('avto.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter = ';', fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(Mylist)):
        writer.writerow(Mylist[i])

#5) Создать json файл с данными о машине.
with open('file_to_json.txt', 'w') as file:
    json.dump(Mylist, file)
