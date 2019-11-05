N = int(input())
def P(n):
    x, y, z = 0, 0, 0
    answer = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(11, 101):
        x = answer[i-5]
        y = answer[i-1]
        z = x+y
        answer.append(z)
    print(answer[n])

for i in range(N):
    x = int(input())
    P(x)