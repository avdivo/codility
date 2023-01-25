def solution(A):
    A.append(0)
    A.sort(reverse=True)
    A = A[:A.index(0)]
    if not A:
        return 1
    return min(set(range(1, max(A)+2)) ^ set(A))

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
