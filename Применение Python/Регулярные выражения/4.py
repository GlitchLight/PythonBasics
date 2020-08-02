# Вам дана последовательность строк. Выведите строки, содержащие обратный слеш "\﻿".

import re
import sys

pattern=r"\\"
for line in sys.stdin:
    line = line.strip()
    lst = re.findall(pattern,line)
    if len(lst) >= 1:
        print(line)
