def fita(x, y, z):
    if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        print('right')
    else:
        print('wrong')

if __name__ == '__main__':
    for i in range(123457):
        a, b, c = map(int, input().split())
        if a == 0:
            exit(0)
        fita(a, b, c)