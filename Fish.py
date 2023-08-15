A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

A = [0, 1]
B = [1, 1]

def solution(A, B):
    stack = []
    fish = 0
    for i in range(len(A)):
        if B[i] == 0:
            while len(stack):
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                fish += 1
        else:
            stack.append(A[i])

    return len(stack) + fish

print(solution(A, B))