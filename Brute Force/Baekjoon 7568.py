n = int(input())
Weight = []
Height = []
key = ''
for k in range(n):
    a, b = map(int, input().split())
    Weight.append(a)
    Height.append(b)

def sol(x, y):
    answer = [1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if(x[i] > x[j] and y[i] > y[j]):
                    answer[j] += 1
    return answer

if __name__ == '__main__':
    result = sol(Weight, Height)
    for k in result:
        key = key + str(k) + ' '
    print(key.rstrip())