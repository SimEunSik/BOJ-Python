def sol(n):
    if n % 5 == 0:
        n //= 5
        print(n)
    elif n % 5 == 1:
        n = (n//5)+1
        print(n)
    elif n % 5 == 2 and n >= 12:
        n = (n//5) +2
        print(n)
    elif n % 5 == 3:
        n = (n//5)+1
        print(n)
    elif n % 5 == 4 and n >= 9:
        n = (n//5)+2
        print(n)
    else:
        print('-1')
if __name__ == '__main__':
    x = int(input())
    answer = sol(x)
