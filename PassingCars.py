def solution(A):
    if 0 not in A:
        return 0
    first_zero = A.index(0)
    all_units = A[first_zero:].count(1)
    counter = 0
    for i in range(first_zero, len(A)):
        if A[i] == 1:
            all_units -= 1
        else:
            counter += all_units
            if counter > 1000000000:
                return -1
    return counter

print(solution([0, 1, 0, 1, 1]))