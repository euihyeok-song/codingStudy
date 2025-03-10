import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int,input().rstrip().split(' '))) for _ in range(N)]
cnt = [0] * 2

def check(x,y,size):
    
    val = paper[y][x]
    
    for ny in range(size):
        for nx in range(size):
            if val != paper[y+ny][x+nx]:
                return False, -1
    return True, val

def recursion(x,y,size):
    
    result, val = check(x,y,size)
    
    if result is True:
        cnt[val] += 1
    else:
        new_size = size//2
        for i in range(2):
            for j in range(2):
                recursion(x+j*new_size,y+i*new_size,new_size)

recursion(0,0,N)

for val in cnt:
    print(val)