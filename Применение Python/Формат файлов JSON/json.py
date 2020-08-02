# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате. <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}] - пример входа

import json

data = input()

class_list = json.loads(data)
class_dict = {}

for i in class_list:
    class_dict[i['name']] = i['parents']

child_dict = {}

for parent in class_dict:
    child_dict[parent] = []
    for possible_child in class_dict:
        for lst_element in class_dict[possible_child]:
            if lst_element == parent:
                child_dict[parent].append(possible_child)


def child_count(name):
    global count
    for local_parent in child_dict[name]:
        if local_parent not in answer_dict:
            answer_dict[local_parent] = ''
            count += 1
            child_count(local_parent)


sorted_child_list = []
for key in child_dict:
    sorted_child_list.append([key, child_dict[key]])
sorted_child_list.sort()
child_dict = {}
for i in range(len(sorted_child_list)):
    child_dict[sorted_child_list[i][0]] = sorted_child_list[i][1]

for element in child_dict:
    count = 1
    answer_dict = {}
    child_count(element)
    print(element, ':', count)