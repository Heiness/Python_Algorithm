# 생각할 경우의 수가 상당히 많다. 포인터를 쓰는 이유와 포인터와 이중포문의 동작을 잘 고려할 것.
import sys; input = sys.stdin.readline
from copy import deepcopy
from pprint import pprint

def move(graph, d): # 0: 상, 1: 하, 2: 좌, 3: 우

    if d==0:
        for j in range(N):
            p = 0
            for i in range(1,N):
                if graph[i][j]:
                    if graph[p][j]==0:
                        graph[p][j]=graph[i][j]
                        graph[i][j]=0 # 아직 합칠 수 있으므로 p증 x
                    elif graph[p][j]==graph[i][j]:
                        graph[p][j]*=2
                        graph[i][j]=0
                        p+=1 # 한번만 합칠수 있으므로
                    else:
                        p+=1
                        # tmp = graph[i][j]
                        # graph[i][j]=0
                        # graph[p][j]=tmp
                        graph[p][j], graph[i][j] = graph[i][j], 0
    
    elif d==1:
        for j in range(N):
            p = N-1
            for i in range(p-1,-1,-1):
                if graph[i][j]:
                    if graph[p][j]==0:
                        graph[p][j]=graph[i][j]
                        graph[i][j]=0
                    elif graph[p][j]==graph[i][j]:
                        graph[p][j]*=2
                        graph[i][j]=0
                        p-=1
                    else:
                        p-=1
                        tmp = graph[i][j]
                        graph[i][j]=0
                        graph[p][j]=tmp
    
    elif d==2:
        for i in range(N):
            p = 0
            for j in range(1,N):
                if graph[i][j]:
                    if graph[i][p]==0:
                        graph[i][p]=graph[i][j]
                        graph[i][j]=0
                    elif graph[i][p]==graph[i][j]:
                        graph[i][p]*=2
                        graph[i][j]=0
                        p+=1
                    else:
                        p+=1
                        tmp = graph[i][j]
                        graph[i][j]=0
                        graph[i][p]=tmp

    elif d==3:
        for i in range(N):
            p = N-1
            for j in range(p-1,-1,-1):
                if graph[i][j]:
                    if graph[i][p]==0:
                        graph[i][p]=graph[i][j]
                        graph[i][j]=0
                    elif graph[i][p]==graph[i][j]:
                        graph[i][p]*=2
                        graph[i][j]=0
                        p-=1
                    else:
                        p-=1
                        tmp = graph[i][j]
                        graph[i][j]=0
                        graph[i][p]=tmp
    
    return graph


def dfs(graph, cnt):
    global ans

    if cnt==5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, graph[i][j])
        return
    else:
        for i in range(4):
            tmp_board = move(deepcopy(graph), i)
            dfs(tmp_board, cnt+1)

ans = 0
N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]

dfs(graph, 0)
print(ans)
