# Вам дана последовательность строк. В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

import sys
import re

pattern = r"human"
for line in sys.stdin:
    line = line.strip()
    line = re.sub(pattern,'computer',line)
    print(line)