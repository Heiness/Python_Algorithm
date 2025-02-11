import sys; input = sys.stdin.readline

N = int(input())


graph = [[] for _ in range(N)]
parents = list(map(int, input().split()))
root_node = 0
delete_node = int(input())


for i in range(N):
    if parents[i] == -1:
        root_node = i
    else:
        if i != delete_node:
            graph[parents[i]].append(i)

if delete_node == root_node:
    print(0)
    exit(0)

res = 0

def dfs(node: int):
    global res

    if len(graph[node]) == 0:
        res += 1
        return
    for n in graph[node]:
        dfs(n)

dfs(root_node)
print(res)