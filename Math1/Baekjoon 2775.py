def sol(x, y):
    apart = [[0] * 15 for a in range(15)]
    for i in range(15):
        apart[0][i] = i
        apart[i][0] = 0
    for j in range(1, 15):
        for k in range(1, 15):
            apart[j][k] = apart[j - 1][k] + apart[j][k - 1]
    print(apart[x][y])

if __name__ == '__main__':
    count = int(input())
    for w in range(count):
        x = int(input())
        y = int(input())
        sol(x, y)