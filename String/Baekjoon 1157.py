from collections import Counter
text = input().upper()
result = Counter(text)
x = list(result.keys())
y = list(result.values())
jax = max(result, key=result.get)
count = 0
for i in y:
    if i == max(y):
        count += 1
if count >= 2:
    print('?')
if count == 1:
    print(jax)