text = input()
count = 0
l1 = ['A', 'B', 'C']
l2 = ['D', 'E', 'F']
l3 = ['G', 'H', 'I']
l4 = ['J', 'K', 'L']
l5 = ['M', 'N', 'O']
l6 = ['P', 'Q', 'R', 'S']
l7 = ['T', 'U', 'V']
l8 = ['W', 'X', 'Y', 'Z']
for i in text:
    if i in l1:
        count += 3
    elif i in l2:
        count += 4
    elif i in l3:
        count += 5
    elif i in l4:
        count += 6
    elif i in l5:
        count += 7
    elif i in l6:
        count += 8
    elif i in l7:
        count += 9
    elif i in l8:
        count += 10
print(count)