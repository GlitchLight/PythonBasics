# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв. За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

s = input()
a = input()
b = input()
count = 0
bad_end = False
while True:
    count += 1
    if count > 1000:
        bad_end = True
        break
    s_count = s.count(a)
    if s_count != 0:
        s = s.replace(a, b)
    else:
        break

if bad_end == True:
    print("Impossible")
else:
    print(count - 1)