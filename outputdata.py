import pandas as pd

def output_student():
    pd.set_option("display.max_columns", None, 'display.max_colwidth', None)
    df = pd.read_csv('students.csv', delimiter= ';')
    print(df)

def select_student():
    df = pd.read_csv('students.csv', delimiter= ';')
    name_student = input('Введите ФИО ученика - ')
    print(df[lambda x: x['ФИО'] == name_student])

def delete_student():
    print('Введите ФИО ученика, данные которого надо удалить')
    del_student = input('-> ')
    df = pd.read_csv('students.csv', delimiter= ';')
    df = df[df.ФИО != del_student]
    df.to_csv(r'students.csv', mode='w', header=True, sep=';', encoding='utf-8', index= False)
    print(df)

def output_places():
    df = pd.read_csv('places.csv', delimiter= ';')
    print(df)

