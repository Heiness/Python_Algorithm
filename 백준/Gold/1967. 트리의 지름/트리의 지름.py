import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, accumulated, visited):
    """
    현재 노드에서 시작해 누적 거리(accumulated)를 기록하며 DFS를 진행합니다.
    각 재귀 호출에서 가장 먼 노드와 해당 거리를 반환합니다.
    """
    visited[node] = True
    farthest_node = node
    max_distance = accumulated
    for child, weight in graph[node]:
        if not visited[child]:
            candidate_node, candidate_distance = dfs(child, accumulated + weight, visited)
            if candidate_distance > max_distance:
                max_distance = candidate_distance
                farthest_node = candidate_node
    return farthest_node, max_distance

# 노드의 개수 입력
n = int(input())
graph = [[] for _ in range(n + 1)]

# 트리 정보 입력 (노드의 개수 - 1 만큼의 간선 정보)
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    # 양방향 연결 (트리이므로 양쪽 모두 연결)
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

# 1번 노드에서 시작하여 가장 멀리 있는 노드 찾기
visited = [False] * (n + 1)
farthest_node, _ = dfs(1, 0, visited)

# 찾은 노드에서 시작하여 가장 멀리 있는 거리(트리의 지름) 계산
visited = [False] * (n + 1)
_, diameter = dfs(farthest_node, 0, visited)

print(diameter)