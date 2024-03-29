import sys; input = sys.stdin.readline

L = int(input())
S = input().strip()

def makePIArr(S):
  table = [0] * len(S); i = 0
  for j in range(1, len(S)):
    while i>0 and S[i]!=S[j]: i = table[i-1]
    if S[i]==S[j]:
      i+=1
      table[j]=i
  
  print(L-table[-1])
  
makePIArr(S)