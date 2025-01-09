N, L = map(int,input().split())
leak = list(map(int,input().split()))
leak.sort()

start = leak[0]
count = 1

for i in range(1,len(leak)):
    if (leak[i]+0.5)-(start-0.5) <= L:
        continue
    else:
        start = leak[i]
        count += 1
print(count)