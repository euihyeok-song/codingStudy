import sys

def custom_key(tmp):
    
    total = 0
    for i in tmp:
        if ord(i) - 65 < 0:
            total += int(i)
    
    return total
    

input = sys.stdin.readline

N = int(input().rstrip())
arr = []

for i in range(N):
    arr.append(input().rstrip())

arr.sort(key=lambda x: (len(x),custom_key(x),x))

for val in arr:
    print(val)