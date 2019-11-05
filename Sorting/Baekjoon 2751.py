import sys
n = int(sys.stdin.readline())
answer = []
for i in range(n):
    answer.append(int(sys.stdin.readline()))
print(*sorted(answer), sep='\n')