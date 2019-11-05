import math
count = int(input())
case = []
for q in range(count):
    case.append(input())

def sol(n):
    a, b = n.split()
    a = int(a)
    b = int(b)
    dis = b - a
    answer = 0
    lin = 0
    for i in range(2**31):
        if dis <= 2:
            print(dis)
            break
        if dis <= i**2:
            lin = 2*i-1
            dis = dis - (i-1)**2
            re = math.floor(dis // i)
            answer = lin + re - 1
            print(answer)
            break

if __name__ == '__main__':
    for i in case:
        sol(i)