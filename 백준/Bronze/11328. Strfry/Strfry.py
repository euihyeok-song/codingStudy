N = int(input())

for _ in range(N):
    
    first, second = input().split(' ')

    if sorted(first) == sorted(second):
        print("Possible")
    else:
        print("Impossible")