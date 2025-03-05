import sys

input = sys.stdin.readline

A,B,C = map(int,input().rstrip().split(' '))

def pow(A,B,C):

    if B == 1:
        return (A%C)
    
    # A^2 % C를 (A%C)*(A*C)%C로 나눔
    num = pow(A,B//2,C)
    
    if B % 2 == 0:
        return (num * num) % C
    else:
        return ((num * num) % C) * A % C

print(pow(A,B,C))