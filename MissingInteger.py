import random, time


def solution(A):
    # ts = time.time()
    # clear = set(filter(lambda x: x > 0, A))
    # print(time.time() - ts)
    #
    # ts = time.time()
    # print(time.time() - ts)
    # if not clear:
    #     return 1
    # out = min(set(range(1, max(clear)+2)) ^ clear)
    # print(time.time() - ts)
    #
    # return out

    clear = sorted(list(set(filter(lambda x: x > 0, A))))
    for i in range(len(clear)+1):
        try:
            if i+1 != clear[i]:
                return i + 1
        except:
            return i + 1



s = [random.randint(0, 10000) for _ in range(1000005)]
print(solution(s))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
