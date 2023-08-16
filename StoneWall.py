S = [8, 8, 5, 7, 9, 8, 7, 4, 8]

def solution(S):
    stack = []
    count = 0
    for i in S:
        while stack:
            if stack[-1] == i:
                break
            if stack[-1] < i:
                stack.append(i)
                break
            else:
                stack.pop()
                count += 1
        else:
            stack.append(i)
    while stack:
        stack.pop()
        count += 1

    return count

print(solution(S))