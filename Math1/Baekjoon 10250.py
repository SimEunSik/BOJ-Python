count = int(input())
case = []
for q in range(count):
    case.append(input())

def sol(n):
    x, y, z = n.split()
    x = int(x)
    y = int(y)
    z = int(z)
    room = 1
    mok = z // x
    room += mok
    if z % x == 0:
        room = room - 1
    floor = z % x
    if floor == 0:
        floor = x
    if room < 10:
        print(floor, 0, room, sep='')
    else:
        print(floor, room, sep='')


if __name__ == '__main__':
    for i in case:
        sol(i)