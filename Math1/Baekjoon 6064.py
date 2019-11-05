count = int(input())
case = []
for q in range(count):
    case.append(input())

def sol(n):
    M, N, x, y = map(int, n.split())
    answer = x
    while (answer - y) % N != 0 and answer <= M * N:
        answer += M
    print(-(answer > M * N) or answer)

if __name__ == '__main__':
    for i in case:
        sol(i)