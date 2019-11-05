import sys
input = sys.stdin.readline
N = int(input())
count = [0 for _ in range(10000)]
for i in range(N):
    count[int(input())-1] += 1
for j in range(len(count)):
    for k in range(count[j]):
        print(j+1)