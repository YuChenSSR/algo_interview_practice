import sys

lines = []
for line in sys.stdin:
    line = line.strip()
    if line:
        lines.append(line)

n = int(lines[0])
nums = list(map(int, lines[1].split()))
nums_sum = sum(nums)
sys.stdout.write(str(nums_sum))