from collections import deque
import sys
input = sys.stdin.readline

def is_bipartite_graph(graph, V):
    colors = [0] * (V + 1)  # 0: 방문 안 함, 1: 색1, -1: 색2

    for start in range(1, V + 1):
        if colors[start] == 0:  # 방문하지 않은 정점에 대해 BFS 수행
            queue = deque([start])
            colors[start] = 1  # 시작 정점을 색1로 색칠

            while queue:
                node = queue.popleft()
                current_color = colors[node]

                for neighbor in graph[node]:
                    if colors[neighbor] == 0:  # 방문하지 않은 인접 정점
                        colors[neighbor] = -current_color  # 다른 색으로 색칠
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:  # 인접 정점이 같은 색인 경우
                        return False
    return True

def main():
    K = int(input())  # 테스트 케이스의 수

    for _ in range(K):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V + 1)]

        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        if is_bipartite_graph(graph, V):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
