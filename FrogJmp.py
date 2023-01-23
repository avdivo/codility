def solution(X, Y, D):
    return (Y - X) // D + bool((Y - X) % D)


print(solution(10, 85, 30))