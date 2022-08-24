import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1+min2*2)
        cnt+=1
        if scoville[0]<K and len(scoville)==1:
            return -1
        
    return cnt
