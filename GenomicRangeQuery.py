def solution(S, P, Q):
    answer = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for i in range(len(P)):
        sample = set(S[P[i]:Q[i]+1])
        for k, v in answer.items():
            if k in sample:
                result.append(v)
                break
    return result


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))