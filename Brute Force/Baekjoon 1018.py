def comp(b,t):
    cnt = 0
    for i in range(8):
        if b[i] != t[i]:
            cnt += 1
    return cnt

board = ["WBWBWBWB", "BWBWBWBW"]
n, m = map(int, input().split())
l = []

for i in range(n):
    l.append(str(input()))

x = n-8
y = m-8

case = []
min1 = 64

for i in range(x+1):
    for j in range(y+1):
        l1 = []
        for k in range(8):
            l1.append(l[i+k][j:j+8])
        cnt = 0
        if l1[0][0] == "W":
            for k in range(0, 8, 2):
                cnt += comp(board[0], l1[k])
                cnt += comp(board[1], l1[k+1])
        else:
            for k in range(0, 8, 2):
                cnt += comp(board[1], l1[k])
                cnt += comp(board[0], l1[k+1])
        min1 = min(min1, cnt, 64-cnt)

print(min1)