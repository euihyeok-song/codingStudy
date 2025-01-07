import sys

n = int(sys.stdin.readline().rstrip())
velocity = list(map(int, sys.stdin.readline().rstrip().split()))

result = velocity[-1]

for i in range(n-2, -1, -1):
    if result % velocity[i] != 0:
        result = (result//velocity[i]+1)*velocity[i]
        
print(result)
