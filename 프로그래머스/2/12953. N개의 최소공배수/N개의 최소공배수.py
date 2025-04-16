import math

def solution(arr):
    
    a, b, total = arr[0], 0, 1
    
    for idx in range(1,len(arr)):
        b = arr[idx]
        a = a * b // math.gcd(a,b)
    
    return a