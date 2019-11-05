n = int(input())
answer = []
case = [i for i in range(1, 2700000)]
for i in case:
    i = str(i)
    if '666' in i:
        if i in answer:
            pass
        answer.append(i)
        continue
print(answer[n-1])