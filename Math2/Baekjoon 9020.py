count = int(input())
case = []
for q in range(count):
    case.append(int(input()))

def sosu(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]

def sol(n):
    A = n // 2
    B = A
    if A in X:
        print(A, A, sep=' ')
    elif A not in X:
        while A > 0 and B > 0:
            A -= 1
            B += 1
            if A in X and B in X and A + B == n:
                print(A, B, sep=' ')
                break

if __name__ == '__main__':
    X = sosu(10000)
    for i in case:
        sol(i)