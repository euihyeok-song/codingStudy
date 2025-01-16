n = int(input())
num = list(map(int, input().split(' ')))
x = int(input())

count = 0
start = 0
end = n-1

# 오름차순 정렬
num.sort()

while(start < end):
    
    result = num[start] + num[end]
    
    if result == x:
        start += 1
        count += 1
    elif result < x:
        start += 1
    else:
        end -= 1
    
print(count)
    