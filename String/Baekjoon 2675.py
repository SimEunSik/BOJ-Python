count = int(input())
case = []
for j in range(count):
    case.append(input())

def Re(n):
    x, y = n.split()
    x = int(x)
    z = []
    for i in range(len(y)):
        z.append(y[i] * x)
    answer = "".join(map(str, z))
    print(answer)

for i in case:
    Re(i)
