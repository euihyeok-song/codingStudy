import sys

def hanoi(st,en,tmp,N):
    if N == 1:
        print(st,en)
    else:
        hanoi(st,tmp,en,N-1)
        print(st,en)
        hanoi(tmp,en,st,N-1)
    

input = sys.stdin.readline

N = int(input())
print(2**N-1)

hanoi(1,3,2,N)