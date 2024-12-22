N = int(input())

num = list(map(int, input().split(' ')))

for i in range(2):
    
    if i==1:
        print(max(num))
    else:
        print(min(num), end=' ')