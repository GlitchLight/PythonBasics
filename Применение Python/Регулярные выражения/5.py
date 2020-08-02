# Вам дана последовательность строк. Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

import re
import sys

pattern = r"\b(\w+)\1\b"
for line in sys.stdin:
    line = line.strip()
    num = re.findall(pattern,line)
    if len(num) >= 1:
        print(line)
