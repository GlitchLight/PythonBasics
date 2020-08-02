# Вам дана последовательность строк. Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

import sys
import re

pattern = r"z\w{3}z"
for line in sys.stdin:
    line = line.strip()
    num = re.findall(pattern,line)
    if len(num) >= 1:
        print(line)