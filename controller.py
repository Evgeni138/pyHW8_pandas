from inputdata import input_student
from inputdata import input_place_class
from outputdata import output_student
from outputdata import select_student
from outputdata import delete_student
from outputdata import output_places
from merge_tables import physics
from merge_tables import chemisry

def start():
      instruction = ''
      while instruction != 'n':
            print('Выберите действие:\n'
                  '1 - Вывести список всех учеников\n'
                  '2 - Вывести нужного ученика\n'
                  '3 - Внести нового ученика\n'
                  '4 - Удалить ученика\n'
                  '5 - Внести новое место в классе\n'
                  '6 - Вывести все места в классе\n'
                  '7 - Вывести рассадку мест в классе на физике\n'
                  '8 - Вывести рассадку мест в классе на химии\n'
                  'n - Для выхода из программы')
            instruction = input('-> ')
            if (instruction == '1'):
                  output_student()
            elif (instruction == '2'):
                  select_student()
            elif (instruction == '3'):
                  input_student()
            elif (instruction == '4'):
                  delete_student()
            elif (instruction == '5'):
                  input_place_class()
            elif (instruction == '6'):
                  output_places()
            elif (instruction == 'n'):
                  print('Досвидания!')
            elif (instruction == '7'):
                  physics()
            elif (instruction == '8'):
                  chemisry()
            else:
                  print('Введите корректную команду')

