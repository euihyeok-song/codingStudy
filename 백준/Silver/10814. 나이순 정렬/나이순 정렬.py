import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = []

for i in range(N):
    age, name = input().rstrip().split(' ')
    arr.append([int(age),name])
    
for age,name in sorted(arr, key=lambda x : x[0]):
    print(age,name)