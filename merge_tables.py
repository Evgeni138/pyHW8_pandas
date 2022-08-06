import pandas as pd

def physics():
    df1 = pd.read_csv('students.csv', delimiter= ';')
    df2 = pd.read_csv('places.csv', delimiter= ';')
    df_physics = df1.merge(df2, how= 'left', left_on= 'Место на физике', right_on= 'ID места')
    df_physics = df_physics.drop(columns= ['ID уч.', 'Год рожд.', 'Статус', 'Место на химии', 'ID места'], axis= 1)
    print(df_physics)

def chemisry():
    df1 = pd.read_csv('students.csv', delimiter= ';')
    df2 = pd.read_csv('places.csv', delimiter= ';')
    df_chemistry = df1.merge(df2, how= 'left', left_on= 'Место на химии', right_on= 'ID места')
    df_chemistry = df_chemistry.drop(columns= ['ID уч.', 'Год рожд.', 'Статус', 'Место на физике', 'ID места'], axis= 1)
    print(df_chemistry)
