N = int(input())
E = int(input())

array = [[0] for _ in range(N+1)]
last = 0

for _ in range(E):
    
    schedule = list(map(int,input().split(' ')))
    
    # 선영이가 포함되어 있다면
    if 1 in schedule[1:]:
        for i in range(1,schedule[0]+1):
            array[schedule[i]].append(last+1)
        last += 1

    # 선영이가 포함되어 있지 않다면
    else:
        total = []
        for j in range(1,schedule[0]+1):
            total += array[schedule[j]]
        
        for k in range(1, schedule[0]+1):
            array[schedule[k]] = list(set(total))

for idx,val in enumerate(array):
    
    if val == array[1]:
        print(idx)