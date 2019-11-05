count = int(input())
case = list(map(int, input().split()))

def sosu(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]

if __name__ == '__main__':
    re = 0
    for i in case:
        sosu(i)
        if i in sosu(i):
            re += 1
    print(re)