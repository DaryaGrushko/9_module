# Декораторы
def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        d = 2
        while result % d != 0:
           # print('d=', d)
            d += 1
        if d == result:
            print(f'{result} - Простое число')

        else:
            print(f'{result} - Составное число')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)

print(result)

