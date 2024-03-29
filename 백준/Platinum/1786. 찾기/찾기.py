# import sys; input = sys.stdin.readline

T = input()
P = input()

def KMP(T,P):
  table = [0 for _ in range(len(P))]
  i = 0
  for j in range(1, len(P)):
    while i>0 and P[i] != P[j]: i = table[i-1]
    if P[i]==P[j]:
      i+=1
      table[j]=i
      
  result = []
  i = 0
  for j in range(len(T)):
    while i>0 and P[i] != T[j]: i = table[i-1]
    if P[i] == T[j]:
      i+=1
      if i==len(P):
        result.append(j-i+2)
        i = table[i-1]
  
  print(len(result))
  print(*result)

KMP(T,P)