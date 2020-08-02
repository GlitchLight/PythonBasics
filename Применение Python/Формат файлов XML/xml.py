# Вам дано описание пирамиды из кубиков в формате XML. Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿). 
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. 
# Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д. Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

# Пример входа <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

from xml.etree import ElementTree

s = input()
root = ElementTree.fromstring(s)

d = {'red': 0,'green': 0,'blue': 0}

d[root.attrib['color']] +=1

level = 1
def color_counter(level, child):
    level += 1
    d[child.attrib['color']] += level
    for child_child in child:
        color_counter(level, child_child)

for child in root:
    color_counter(level, child)

for key in d:
    print(d[key], end = ' ')