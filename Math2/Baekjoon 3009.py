case = []
for i in range(3):
    a, b = map(int, input().split())
    case.append(a)
    case.append(b)

x = 0
y = 0
if case[0] == case[2] and case[0] != case[4]:
    x = case[4]
elif case[0] != case[2] and case[0] == case[4]:
    x = case[2]
elif case[0] != case[2] and case[2] == case[4]:
    x = case[0]

if case[1] == case[3] and case[1] != case[5]:
    y = case[5]
elif case[1] != case[3] and case[1] == case[5]:
    y = case[3]
elif case[1] != case[3] and case[3] == case[5]:
    y = case[1]

print(x, y, sep=' ')