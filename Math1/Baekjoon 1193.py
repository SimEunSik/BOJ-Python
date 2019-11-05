def sol(n):
    a = 0
    if n <= 2:
        print(1, '/', n, sep='')
        pass
    for i in range(1, n):
        a = a + i
        if a >= n and n >= 3:
            a = a - i
            a = n - a
            b = (i+1) - a
            if i % 2 == 0:
                print(a, '/', b, sep='')
                break
            elif i % 2 == 1:
                print(b, '/', a, sep='')
                break

if __name__ == '__main__':
    x = int(input())
    answer = sol(x)