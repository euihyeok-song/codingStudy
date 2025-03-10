import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip().split(' '))) for _ in range(N)]
cnt = [0] * 3
def check(x,y,size):
    
    val = graph[y][x]
    
    for i in range(y,y+size):
        for j in range(x,x+size):
            if val != graph[i][j]:
                return False, 0

    return True, val
            

def recurison(x,y,size):
    
    result, val = check(x,y,size)
    
    if result is True:
        cnt[val] += 1
        return
    else:
        new_size = size//3
        for ny in range(3):
            for nx in range(3):
                recurison(x + nx * new_size ,y + ny * new_size ,new_size)

recurison(0,0,N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])