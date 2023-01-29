def solution(A, B):
    turn = 0
    while turn < len(B):
        offset = len(B) - turn % len(B)
        for i, dish in enumerate(A):
            if dish == B[(offset+i)%len(A)]:
                break
        else:
            return turn
        turn += 1
    return -1


print(solution([1, 3, 5, 2, 8, 7], [7, 1, 9, 8, 5, 7]))
print(solution([1, 1, 1, 1], [1, 2, 3, 4]))
print(solution([3, 5, 0, 2, 4], [1, 3, 10, 6, 7]))


