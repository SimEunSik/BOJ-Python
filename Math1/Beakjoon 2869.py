def sol(x, y, z):
    answer = (z - y) // (x - y)
    look = (z - y) % (x - y)
    if look != 0:
        answer += 1
        print(answer)
        pass
    else:
        print(answer)

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    answer = sol(a, b, c)