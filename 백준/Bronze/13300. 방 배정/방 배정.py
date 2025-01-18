N, K = map(int, input().split(' '))

dic = dict({10:0, 11:0, 20:0, 21:0, 30:0, 31:0, 40:0, 41:0, 50:0, 51:0, 61:0, 60:0})

cnt = 0

for _ in range(N):
    
    S, Y = map(int, input().split(' '))
    
    dic[10*Y + S] += 1

for key in dic:
    
    if dic[key] % K != 0:
        cnt += dic[key] // K + 1
    else:
        cnt += dic[key] // K

print(cnt)