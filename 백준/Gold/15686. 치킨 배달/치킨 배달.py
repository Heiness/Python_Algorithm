import sys

input = sys.stdin.readline

INF = 99999


def get_path_graph():
    graph = [[] for _ in range(stores_n)]  # row: store, col: house
    for s in range(stores_n):
        for h in range(houses_n):
            graph[s].append(abs(stores[s][0] - houses[h][0]) + abs(stores[s][1] - houses[h][1]))
    return graph


def dfs(depth, index, combination):
    if depth >= M:
        combinations.append(combination.copy())
        return

    for s in range(index, stores_n):
        combination.append(s)
        dfs(depth + 1, s + 1, combination)
        combination.pop()


def solve():
    answer = INF
    for combination in combinations:
        result = [INF] * houses_n
        for s in combination:
            for h in range(houses_n):
                result[h] = min(result[h], path_graph[s][h])
        answer = min(answer, sum(result))
    return answer


# main
N, M = map(int,input().split())
stores = []
houses = []
stores_n = 0
houses_n = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            stores.append((i, j))
            stores_n += 1
        elif row[j] == 1:
            houses.append((i, j))
            houses_n += 1

path_graph = get_path_graph()
combinations = []
dfs(0, 0, [])
print(solve())