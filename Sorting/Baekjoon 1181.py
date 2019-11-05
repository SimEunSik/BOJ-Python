import operator
n = int(input())
case = set(list(str(input()) for _ in range(n)))
answer = []
for i in case:
    answer.append([len(i), i])
answer = sorted(answer, key=operator.itemgetter(1))
answer = sorted(answer, key=operator.itemgetter(0))
for j in range(len(answer)):
    print(answer[j][1])