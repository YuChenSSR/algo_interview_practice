"""
Multiple sets A+B Zero tail mode
给定若干组测试数据，最后一组数据为 0 0，作为输入的结尾。

每组数据有两个整数a 和b，请你求出 a+b 的值。
输入描述：

每行有两个整数 a （0≤a ≤ 10^9）和6（0≤6≤10^9）。

最后一组数据为 0 0，作为输入的结尾。

输出描述：

输出若干行，每行一个整数，代表a+b的值。
"""

import sys

ans = []

for line in sys.stdin:
    if not line.strip():
        continue
    parts = line.split()
    if len(parts) != 2:
        continue
    a, b = map(int, parts)
    if a == 0 and b == 0:
        break
    ans.append(str(a+b))
    
sys.stdout.write("\n".join(ans))

