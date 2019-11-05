num1, num2 = input().split()
def cut(n):
    ch = []
    ch.append(n[:1])
    ch.append(n[1:2])
    ch.append(n[2:])
    a = list(reversed(ch))
    a = a[0]+a[1]+a[2]
    return a

x = cut(num1)
y = cut(num2)
if x > y:
    print(x)
else:
    print(y)