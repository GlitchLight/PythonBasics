# Вам дана последовательность строк. В каждой строке замените все вхождения нескольких одинаковых букв на одну букву. Буквой считается символ из группы \w.

import re
import sys

pattern = r'(\w)(\1+)'
for line in sys.stdin:
    line = line.strip()
    line = re.sub(pattern, r'\1', line)
    print(line)
