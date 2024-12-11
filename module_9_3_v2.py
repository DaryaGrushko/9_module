# Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) for x,y in zip(first, second) if len(x) != len(y))
second_result = (len(first[x]) == len(second[x]) for x in range (len(first)))

for elem in first_result:
    print(elem, end = ' ') #посчиталось только что
print ()

for elem in second_result:
    print(elem, end = ' ') #посчиталось только что


