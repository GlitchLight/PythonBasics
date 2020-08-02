# Вашей программе на вход подаются две строки, содержащие url двух документов A и B. Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
import re

import requests

link1 = input().strip()
link2 = input().strip()

end = False
pattern = r'<a href="(\S+)">'
res = re.findall(pattern, requests.get(link1).content.decode("utf-8"))

for i in res:
    res_inside = re.findall(pattern, requests.get(i).content.decode("utf-8"))
    for j in res_inside:
        if j == link2:
            print('Yes')
            end = True
            break
    if end == True:
        break

if end == False:
    print('No')


