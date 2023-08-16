from collections import Counter


A = [3, 4, 3, 2, 3, -1, 3, 3]


def dominator(A):
    if not A:
        return -1
    count = Counter(A)
    a = count.most_common(1)
    if a[0][1] <= len(A)//2:
        return -1
    return A.index(a[0][0])


print(dominator(A))
