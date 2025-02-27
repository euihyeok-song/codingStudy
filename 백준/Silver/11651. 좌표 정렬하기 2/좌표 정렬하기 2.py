import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = []

for i in range(N):
    arr.append(list(map(int,input().rstrip().split(' '))))
    
for x,y in sorted(arr, key=lambda x: (x[1],x[0])):
    print(x, y)