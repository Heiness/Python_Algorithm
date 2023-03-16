import heapq
import sys;input = sys.stdin.readline

cards = []
result = 0


for i in range(int(input())): 
    heapq.heappush(cards, int(input()))

if len(cards) != 1:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)

print(result)
