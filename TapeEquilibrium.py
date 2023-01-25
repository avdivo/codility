def solution(A):
    l = A[0]
    r = sum(A[1:])
    m = 1000000000
    for i in range(1, len(A)):
        if abs(l-r) < m:
            m = abs(l - r)
            if m == 0:
                break
        l += A[i]
        r -= A[i]
    return m


print(solution([3, 1, 2, 4, 3]))

