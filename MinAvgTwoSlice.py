def solution(A):
    s = 0
    pref_sum = []
    for i in A:
        s = s + i
        pref_sum.append(s)

    min_avg = 50000
    start = 0

    for i in range(len(pref_sum)-1):
        base = pref_sum[i-1] if i else 0
        if (pref_sum[i+1] - base) / 2 < min_avg:
            min_avg = (pref_sum[i+1] - base) / 2
            start = i
        if i < len(pref_sum)-2 and (pref_sum[i+2] - base) / 3 < min_avg:
            min_avg = (pref_sum[i+2] - base) / 3
            start = i

    return start


print(solution([4, 3, 3, 5, 1, 5, 8]))