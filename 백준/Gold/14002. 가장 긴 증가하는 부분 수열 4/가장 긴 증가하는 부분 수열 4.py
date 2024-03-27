import sys; input = sys.stdin.readline
from bisect import bisect_left

def main():
    N = int(input())
    *A, = map(int, input().split())

    LIS = [1, ]
    substr = [A[0]]
    for i in range(1, N):
        if A[i] > substr[-1]:
            substr.append(A[i])
            LIS.append(len(substr))
        else:
            l = bisect_left(substr, A[i])
            substr[l] = A[i]
            LIS.append(l+1) 
    j = len(substr)
    ans = [0]*len(substr)
    i = N-1
    while i >= 0:
        if LIS[i] == j:
            j -= 1
            ans[j] = A[i]
        i -= 1
    print(len(ans))
    print(*ans)
    return

main()