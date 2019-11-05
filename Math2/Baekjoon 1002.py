import math
count = int(input())
case = []
for q in range(count):
    case.append(input())

def sol(n):
    x1, y1, r1, x2, y2, r2 = map(int, n.split())
    dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dis == 0 and r1 == r2:
        print('-1')
    elif dis + r1 == r2 or dis + r2 == r1 or r1 + r2 == dis:
        print('1')
    elif r1 + r2 < dis or dis + r1 < r2 or dis + r2 < r1:
        print('0')
    else:
        print('2')

if __name__ == '__main__':
    for i in case:
        sol(i)