T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))
def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return a, b
for i in N:
    if i == 0:
        print('1 0')
    elif i == 1:
        print('0 1')
    else:
        x, y = fibonacci(i)
        print(x, y)