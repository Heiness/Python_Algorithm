import sys; input = sys.stdin.readline

def bs(arr, target):
    start, end = 0, N - 1
    
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target: return 1

        if arr[mid] > target: end = mid - 1
        else: start = mid + 1

    return 0

T = int(input())

for _ in range(T):
    N = int(input())
    arrN = list(map(int, input().split()))
    M = int(input())
    arrM = list(map(int, input().split()))

    arrN.sort()


    for num in arrM:
        print(bs(arrN, num))