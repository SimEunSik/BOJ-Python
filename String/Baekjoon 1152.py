from collections import Counter
text = input().upper().split()
count = Counter(text)
answer = 0
for key in count:
    if key == '':
        continue
    answer += count[key]
print(answer)