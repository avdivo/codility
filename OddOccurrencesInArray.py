from collections import Counter


def solution(A):
    c = Counter(A)
    for k, v in c.items():
        if v%2:
            return k


print(solution([9,3,9,3,9,7,9]))