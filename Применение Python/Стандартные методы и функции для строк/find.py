# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв. Выведите одно число – количество вхождений строки t в строку s.

s=input()
t=input()

count=-1
value=0
begin=0
while value!=-1:
    count+=1
    value = s.find(t, begin)
    begin = value + 1

print(count)