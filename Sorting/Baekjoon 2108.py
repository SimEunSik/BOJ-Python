import sys
from collections import Counter
n = int(sys.stdin.readline())
answer = []
for i in range(n):
    answer.append(int(sys.stdin.readline()))

def san(a ,n):
    result = sum(n) / a
    return round(result)

def joong(n):
    result = n.sort()
    result = n[len(n) // 2]
    return result

def choi(n):
    c = Counter(n)
    order = c.most_common()
    maxa = order[0][1]
    modes = []
    for num in order:
        if num[1] == maxa:
            modes.append(num[0])
    modes.sort()
    if len(modes) == 1:
        result = modes[0]
    else:
        result = modes[1]
    return result

def beom(n):
    result = n[-1] - n[0]
    return result

print(san(n, answer))
print(joong(answer))
print(choi(answer))
print(beom(answer))