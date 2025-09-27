
from os import error
from ast import Num
import sys


n_number = []
i = 0
sums = []
for line in sys.stdin:
    if not line.strip():
        continue
    line = line.strip()
    if i == 0:
        t = int(line)
    elif i%2 == 0 and i != 0:
        line = line.split()
        line_intlst = map(int, line)
        sums.append(sum(line_intlst))
    elif i%2 == 1:
        n = int(line)
        n_number.append(n)
    i += 1

try:
    if sum(n_number) > 100000:
        raise Exception("The sum of n is too large.")
    
    sys.stdout.write("\n".join(map(str,sums)))

except Exception as e:
    sys.stdout.write(f"程序异常退出{e}\n")


