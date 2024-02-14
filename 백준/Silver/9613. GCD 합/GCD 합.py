# GCD의 합
# GCD란 최대 공약수
# 1. math를 이용한 gcd함수를 이용해서 계산

import math
import sys

times = int(input())

ans = []

for i in range(times):
    
    result = 0
    
    case = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    
    n = len(case)-1
    
    for i in range(1,n):
        for j in range(i+1,n+1):
            result += math.gcd(case[i],case[j])
    ans.append(result)
            

for k in range(len(ans)):
    print(ans[k])
