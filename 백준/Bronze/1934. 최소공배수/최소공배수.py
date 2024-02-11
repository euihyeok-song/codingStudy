# 최소공배수
import math
import sys

times = int(input())

for i in range(times):

    number = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    X = number[0]
    Y = number[1]
    
    print(math.lcm(X, Y))
    
