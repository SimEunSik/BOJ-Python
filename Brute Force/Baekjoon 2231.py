n = int(input())
answer = []
if n <= 1000000 and n >= 1:
    for i in range(1, n+1):
        sum = 0
        sum = sum + i
        i = str(i)
        for j in i:
            sum = sum + int(j)
            if sum == n and j == i[-1]:
                answer.append(i)
                print(answer[0])
                exit(0)
    if i == n or len(answer) == 0:
        print('0')
        exit(0)