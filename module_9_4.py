# Создание функций на лету
# Задача "Функциональное разнообразие"

from random import choice

print ('------Задача - lambda-функция  -------------')

first = 'Мама мыла раму'
second = 'Рамена мало было'

print (list(map(lambda x,y : x == y, first, second)))


print ('------Задача - Замыкание  -------------')

def get_advanced_writer(file_name):

    def  write_everything(*data_set):
        for data in data_set:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(str(data) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


print ('------Задача - class  MysticBall -------------')
class  MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())

