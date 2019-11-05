def Group(n):
    number = 0
    for i in n:
        number += zip(i)
    return number

def zip(sentence):
    count = 1
    next = ""
    result = ""
    for i in sentence:
        if next != i and i not in result:
            next = i
            result += i
        if next != i and i in result:
            count = 0
            break
        if next == i:
            continue
    return count

if __name__ == '__main__':
    num = int(input())
    case = []
    for j in range(num):
        case.append(input())
    answer = Group(case)
    print(answer)