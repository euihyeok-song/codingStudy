# 최댓값 => dfs or bfs

N, M = map(int, input().split())

cost = []
totalCost = [0] * M

for _ in range(M):
    cost.append(int(input()))
    
sortCost = sorted(cost)    

# 달걀 갯수가 사람 수보다 많은 경우
if N >= M:
    for i in range(M):
        totalCost[i] = sortCost[i] * (M - i)
# 달걀 갯수가 사람 수보다 작은 경우
else:
    for j in range((M-N),M):
        totalCost[j] = sortCost[j] * (M - j)
        
print(sortCost[totalCost.index(max(totalCost))], max(totalCost))


