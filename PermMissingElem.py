def solution(A):
    n = len(A)+1
    result = n * (n + 1)//2

    return result - sum(A)
print(solution([2, 3, 4, 1, 6]))

