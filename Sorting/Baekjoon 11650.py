import sys
import operator
n = int(sys.stdin.readline())
case = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    case.append([x, y])
case = sorted(case, key=operator.itemgetter(1))
case = sorted(case, key=operator.itemgetter(0))
for i in range(n):
    print(case[i][0], case[i][1])