import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    MIN = float('inf')
    cache = {0: 0}
    for memory, cost in zip(map(int, input().split()), map(int, input().split())):
        temp = {}
        for key, value in cache.items():
            if memory + value >= M:
                MIN = min(MIN, cost + key)
            elif cache.get(cost + key, 0) < memory + value:
                temp[cost + key] = memory + value
        cache.update(temp)
    return MIN


print(solution())