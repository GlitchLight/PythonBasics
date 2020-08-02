# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

def primes():
    a = 1
    while True:  # просто пример
        a += 1
        Fail = False
        for i in range(2, a):
            if (a % i == 0) & (i != a):
                Fail = True
                break
        if Fail == True:
            continue
        else:
            Fail == False
            yield a
