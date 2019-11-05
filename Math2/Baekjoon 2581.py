X = int(input())
Y = int(input())

def sosu(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]

if __name__ == '__main__':
   A = sosu(X)
   B = sosu(Y)
   for i in A:
       B.remove(i)
   if X in A and X != Y:
       B.insert(0, X)
   if sum(B) == 0:
       print('-1')
   else:
    print(sum(B))
    print(B[0])