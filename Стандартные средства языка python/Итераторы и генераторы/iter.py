# Одним из самых часто используемых классов в Python является класс filter. 
# Он принимает в конструкторе два аргумента a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из последовательности a, что f(x) равно True. 
# Будем говорить, что в этом случае функция f допускает элемент x, а элемент x является допущенным. 
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный класс filter, но будет использовать не одну функцию, а несколько.
# Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько не допускают. Обозначим эти количества за pos и neg.
# Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает True, если элемент допущен, и False иначе.

class multifilter():
    def judge_half(pos, neg):
        if pos >= neg:
            return True

    def judge_any(pos, neg):
        if pos >= 1:
            return True

    def judge_all(pos, neg):
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge = judge_any):
        self.iterable = iterable
        lst_funcs = [*funcs]
        self.funcs = lst_funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos = 0
            neg = 0
            for j in self.funcs:
                if j(i) == True:
                    pos += 1
                else:
                    neg += 1
            k = self.judge(pos, neg)

            if k == True:
                yield(i)