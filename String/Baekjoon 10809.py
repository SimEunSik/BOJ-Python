x = input()
answer = [-1]*26
for i in x:
    if answer[ord(i)-97] is -1:
        answer[ord(i) - 97] = x.index(i)
answer = " ".join(map(str, answer))
print(answer)