# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный 
# математический факт об этом числе. Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе. Выводите информацию об интересности чисел
# в таком же порядке, в каком следуют числа во входном файле.

import sys

import requests

api_url = r"http://numbersapi.com"

a = []
for number in sys.stdin:
    a.append(number.rstrip())

params = {
    'number': 'integer',
    'type': 'math',
    'json': 'true'
}

for i in a:
    api_url_new = ''
    api_url_new = api_url + '/' + i
    res = requests.get(api_url_new, params=params)
    data = res.json()
    if data["found"]:
        print('Interesting')
    else:
        print('Boring')
