def sosu(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]

def find(n):
    A = len(sosu(n))
    B = len(sosu(2*n))
    print(B-A)

if __name__ == '__main__':
    for i in range(123457):
        n = int(input())
        if n == 0:
            exit(0)
        find(n)