# Вам дана последовательность строк. Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import sys
import re

pattern = "cat"
for line in sys.stdin:
    line = line.rstrip()
    num = re.findall(pattern, line)
    if len(num) >= 2:
        print(line)