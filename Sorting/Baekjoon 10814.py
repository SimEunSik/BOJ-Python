import sys
import operator
n = int(sys.stdin.readline())
case = []
for _ in range(n):
    x, y = map(str, sys.stdin.readline().split())
    x = int(x)
    case.append([x, y])
case = sorted(case, key=operator.itemgetter(0))
for i in range(n):
    print(case[i][0], case[i][1])