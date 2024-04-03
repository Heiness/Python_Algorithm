import sys

input = sys.stdin.readline 

d = dict()
d['U'] = (-1, 0)
d['D'] = (1, 0)
d['R'] = (0, 1)
d['L'] = (0, -1)

res = 0
def dfs(x, y, board, visited, fin):

  global res
  visited[x][y] = 1
  dx, dy = d[board[x][y]]
  nx = x + dx
  ny = y + dy

  if visited[nx][ny] == 0:
    dfs(nx, ny, board, visited, fin)
  else:
    if fin[nx][ny] == 0:
      res += 1


  fin[x][y] = 1
def solution(n, m, board):
  visited=  [[0] * m for _ in range(n)]
  fin = [[0] * m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if visited[i][j] == 0:

        dfs(i, j, board, visited, fin)

  return res
if __name__ == "__main__":
  n, m = map(int, input().strip().split())
  board = []
  for _ in range(n):
    board.append(list(input().strip()))
  print(solution(n, m, board))