T = int(input())

for _ in range(T):
    
    n = int(input())
    
    clothes = dict()
    
    for i in range(n):
        
        name, kind = input().split(' ')
        
        clothes[kind] = clothes.get(kind, 0) + 1

    num = list(clothes.values())
    totalCase = 1
    
    # 0을 포함해서 생각하기
    for j in num:
        totalCase *= (j+1)
        
    print(totalCase-1)
    
    