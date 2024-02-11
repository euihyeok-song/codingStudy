#최소공배수 구하기3
# 유클리드 호제법으로 구하기

import sys

times = int(input())

# 최대공약수
def gcd(a,b):
    while(b != 0):
        a, b = b, a % b
    return a

# 최소공배수
def lcm(a,b,g):
    return int(g * (a/g) * (b/g))
    

for i in range(times):
    
    number = list(map(int,sys.stdin.readline().rstrip('/n').split(' ')))
    
    X = number[0]
    Y = number[1]
    
    gc = gcd(X,Y)
    lc = lcm(X, Y, gc)
    
    print(lc)