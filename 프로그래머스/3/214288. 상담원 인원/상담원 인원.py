from itertools import combinations_with_replacement
from heapq import heappush, heappop
import sys

def simulate(mentors, reqs, k):
    # 각 상담 유형별 대기 시간 합계
    total_wait = 0
    for i in range(1, k+1):
        queue = []
        available = []  # 멘토가 상담 가능한 시간 저장
        for _ in range(mentors[i]):
            heappush(available, 0)

        for a, b, c in reqs:
            if c != i:
                continue
            start_time = a
            duration = b

            # 가장 먼저 상담 가능한 멘토 시간 확인
            available_time = heappop(available)
            if available_time <= start_time:
                # 즉시 상담 가능
                heappush(available, start_time + duration)
            else:
                # 대기 필요
                wait = available_time - start_time
                total_wait += wait
                heappush(available, available_time + duration)
    return total_wait

def solution(k, n, reqs):
    # 상담 유형 수 = k, 멘토 수 = n
    base = [1] * k  # 최소 1명씩 배정
    rest = n - k  # 남는 멘토 수

    min_wait = sys.maxsize

    def dfs(idx, left, current):
        nonlocal min_wait
        if idx == k:
            if left == 0:
                mentors = {i+1: current[i] for i in range(k)}
                wait_time = simulate(mentors, reqs, k)
                min_wait = min(min_wait, wait_time)
            return
        for i in range(left + 1):
            current[idx] += i
            dfs(idx+1, left - i, current)
            current[idx] -= i

    dfs(0, rest, base[:])

    return min_wait
