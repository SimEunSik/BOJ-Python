def sol(n):
    b = 1
    for i in range(0, n):
        b = b + (6*i)
        if b >= n:
            print(i+1)
            break

if __name__ == '__main__':
    x = int(input())
    answer = sol(x)