# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая будет возвращать True,
# если остаток от деления y на x равен mod, и False иначе.

from functools import partial

def modby(x,m,mod=0):
    if x%m==mod:
        return True
    else:
        return False

def mod_checker(M,MOD=0):
    return (partial(modby,m=M,mod=MOD))