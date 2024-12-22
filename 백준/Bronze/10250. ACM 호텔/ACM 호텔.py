T = int(input())

for _ in range(T):    
    
    H, W, N = map(int, input().split(' '))
    
    floor = N % H
    roomNumber = N // H + 1
    
    if floor == 0:
        floor = H
        roomNumber -= 1
    
    print(100 * floor + roomNumber)