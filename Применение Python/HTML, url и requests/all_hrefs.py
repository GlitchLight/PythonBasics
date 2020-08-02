# Вашей программе на вход подается ссылка на HTML файл. Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > 
# и вывести список сайтов, на которые есть ссылка.

import re

import requests

pattern_type1 = r'<a.*href=\S\b\S*?([\w-]+\.[\w.-]+)\S'
lst = []
d = {}

link = input()
s = requests.get(link).content.decode("utf-8")
ans_1 = re.findall(pattern_type1, s)
ans_1.sort()
for i in ans_1:
    d[i] = ''
for i in d:
    print(i)