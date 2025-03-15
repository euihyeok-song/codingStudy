import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    
    A.sort()
    B.sort()
    
    count = 0
    b_idx = 0
    
    for a in A:
        while b_idx < len(B) and B[b_idx] < a:
            b_idx += 1
        count += b_idx
    
    print(count)