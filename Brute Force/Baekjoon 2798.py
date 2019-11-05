from itertools import combinations
count, num = map(int, input().split())
case = list(map(int, input().split()))
combi = list(combinations(case, 3))
combi = list(map(sum, combi))
combi.sort(reverse=True)
for i in combi:
    if i <= num:
        print(i)
        break