import pandas as pd

def input_student():
    student = {'ID уч.' : [input('Введите номер ученика - ')],
               'ФИО' : [input('Введите ФИО - ')],
               'Год рожд.' : [input('Введите год рождения - ')],
               'Класс': [input('Введите класс ученика - ')],
               'Статус' : [input('Введите статус - ')],
               'Место на физике' : [input('Введите место в классе на физике - ')],
               'Место на химии' : [input('Введите место в классе на химии - ')]}
    df = pd.DataFrame(student)
    df.to_csv(r'students.csv', mode= 'w', header= True, sep= ';', encoding= 'utf-8', index= False)

def input_place_class ():
    place_class = {'ID места' : [input('Введите номер места - ')],
                   'Ряд' : [input('Введите номер ряда - ')],
                   'Парта' : [input('Введите номер парты - ')],
                   'Вариант' : [input('Введите номер варианта - ')]}
    df = pd.DataFrame(place_class)
    df.to_csv(r'places.csv', mode= 'a', header= False, sep= ';', encoding= 'utf-8', index= False)
