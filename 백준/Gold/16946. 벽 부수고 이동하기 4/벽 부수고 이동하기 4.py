import sys
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    graph = [list(input().rstrip()) for _ in range(N)]
    groups, group = [0,0], 2
    def count_group(q, num):
        count = 1
        while q:
            r, c = q.pop()
            for dr, dc in d:
                if 0 <= (nr := r + dr) < N and 0 <= (nc := c + dc) < M:
                    if graph[nr][nc] == "0":
                        count += 1; graph[nr][nc] = num
                        q.append((nr, nc))
        return count % 10
    for r in range(N):
        for c in range(M):
            if graph[r][c] == "0":
                q = [(r, c)]
                graph[r][c] = group
                groups.append(count_group(q, group))
                group += 1
    for r in range(N):
        ans = []
        for c in range(M):
            if graph[r][c] == "1":
                count, tmp = 1, set()
                for dr, dc in d:
                    if 0 <= (nr := r + dr) < N and 0 <= (nc := c + dc) < M:
                        if (t := graph[nr][nc]) != "1": tmp.add(t)
                for n in tmp: count += groups[n]
                ans.append(count % 10)
            else: ans.append("0")
        print("".join(map(str, ans)))
        
if __name__ == "__main__":
    main()