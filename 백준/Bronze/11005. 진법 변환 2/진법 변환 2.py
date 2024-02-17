# 진법 변환 2

# N = 수 / B = 변환할 진법
N, B = map(int,input().split())

remain = []

while(N > 0):
    
    N, r = N//B, N % B
    remain.append(r)
    
remain.reverse()

for i in range(len(remain)):
    
    if(i < len(remain)-1):
        if(remain[i] >= 10):
            remain[i] = chr(remain[i]+55)
        print(remain[i],end='')
    else:
        if(remain[i] >= 10):
            remain[i] = chr(remain[i]+55)
        print(remain[i])
        