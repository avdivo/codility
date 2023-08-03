P = 'amz'
Q = 'amz'

position = list(zip(P, Q))

# Сколько раз конкретная буква может встречаться в строке
letters = dict()
for one, two in position:
    letters.setdefault(one, 0)
    letters[one] += 1
    if one != two:
        letters.setdefault(two, 0)
        letters[two] += 1

# Строим лучшую строку, но поскольку нужно только количество, то можно использовать множество
# В лучшей строке выбираются буквы, которые встречаются чаще всего,
# при одинаковом количестве выбираются буквы, которые уже добавлялись или любая из них, если не добавлялись
string = set()
for one, two in position:
    if letters[one] > letters[two]:
        string.add(one)
    elif letters[one] < letters[two]:
        string.add(two)
    else:
        if one in string:
            continue
        if two in string:
            continue
        string.add(one)

print(len(string))