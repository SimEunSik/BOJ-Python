def BEP(x, y, z):
    if y - z >= 0:
        print('-1')
        return
    answer = x // (z - y) + 1
    print(answer)

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    answer = BEP(a, b, c)
