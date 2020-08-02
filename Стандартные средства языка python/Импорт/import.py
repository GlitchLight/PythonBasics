#  В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день. Во второй строке дано одно число days -- число дней.
#  Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

import datetime

date_list = ([int (i) for i in input().split()])
days = int(input())

date = datetime.date(date_list[0], date_list[1], date_list[2])
delta = datetime.timedelta(days)
date += delta

print(date.year, date.month, date.day)