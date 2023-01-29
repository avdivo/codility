def solution(A, B, K):
    if K == 1:
        return B - A + 1
    first = 0
    while A > first:
        first += K
    return (B - first + 1) // K + bool((B - first + 1) % K)

print(solution(6, 11, 2))