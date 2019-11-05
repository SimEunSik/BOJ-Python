import sys
n = sys.stdin.readline()
case = []
for i in n:
    case.append(i)
case.sort(reverse=True)
print(*case, sep='')