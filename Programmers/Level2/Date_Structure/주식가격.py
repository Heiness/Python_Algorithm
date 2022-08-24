from collections import deque

def solution(prices):
    queue = deque(prices)
    seconds = []

    while len(queue)>0:
        cnt = 0
        price = queue.popleft()
        for i in queue:
            cnt+=1
            if price > i:
                break
                
        seconds.append(cnt)
            
    return seconds