import itertools
import random

# letters = 'abcdefghijklmnopqrst'
# n = 100000
# P = [random.choice(letters) for i in range(n)]
# Q = [random.choice(letters) for i in range(n)]

P = 'dcba'
Q = 'cbad'

P = 'axxz'
Q = 'yzwy'

P = 'xyz'
Q = 'yxe'

P = 'abcdef'
Q = 'bcdefa'

P = 'aaaaabcdd'
Q = 'efghighii'

P = 'bgeafdd'
Q = 'geafddc'

P = 'aaaacbcddd'
Q = 'bbbbacdaaa'

P = 'dddabc'
Q = 'abcefx'

# Переписываем пары букв в set отсортированных кортежей (каждая комбинация получится по 1 разу)
screening = set()
for a in zip(P, Q):
    screening.add(tuple(sorted(a)))

# Готовим словари весов и позиций букв
weight = dict()
position = dict()
for i, (one, two) in enumerate(screening):
    weight.setdefault(one, 0)
    weight[one] += 1
    position.setdefault(one, set())
    position[one].add(i)
    if one != two:
        weight.setdefault(two, 0)
        weight[two] += 1
        position.setdefault(two, set())
        position[two].add(i)
letters = [key for key in weight]

total_len = len(screening)  # Длина строки, которую нужно получить

# Перебираем все комбинации букв, начиная с самых частых. Первая комбинация, которая покроет все позиции
# будет искомой строкой, возвращаем ее длину
for i in range(1, len(screening)+1):
    combinations = itertools.combinations(letters, i)
    for combo in combinations:
        sample = set()
        for l in combo:
            sample = sample.union(position[l])
        if len(sample) == total_len:
            print(i)
            exit()


