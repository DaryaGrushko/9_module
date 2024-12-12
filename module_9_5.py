# Итераторы
# Задача "Range - это просто"

class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):

        if step == 0:
            print ('шаг не может быть равен 0')
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step
        self.start = start
        self.stop = stop
        self.pointer = start
        self.i = 0
        #print('start=', self.start, ', stop =', self.stop, ', step = ', self.step,', pointer = ', self.pointer )

    def __iter__(self):
        self.pointer = self.start
        #print('start=', self.start, ', stop =', self.stop, ', step = ', self.step, ', pointer = ', self.pointer)
        return self

    def __next__(self):


        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
             raise StopIteration()
        else:
            self.pointer += self.step
            return self.pointer - self.step

try:
    print('\n----------Итератор 1:----------')
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
        print('Шаг указан неверно')

print ('\n--------Итератор 2:----------')
try:
    iter2 = Iterator(-5, 1)
    print ('Вывод на консоль: ', end = " ")
    for i in iter2:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

print ('\n--------Итератор 3:----------')
try:
    iter3 = Iterator(6, 15, 2)
    print ('Вывод на консоль: ', end = " ")
    for i in iter3:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

print ('\n--------Итератор 4:----------')
try:
    iter4 = Iterator(5, 1, -1)
    print ('Вывод на консоль: ', end = " ")
    for i in iter4:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

print('\n----------Итератор 5:----------')
try:
    iter5 = Iterator(10, 1)
    print ('Вывод на консоль: ', end = " ")
    for i in iter5:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')





