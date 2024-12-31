M = int(input())
scores = list(map(int, input().split()))
result = max(scores)

for i in range(M):
    scores[i] = scores[i]/result*100

print(sum(scores)/M)