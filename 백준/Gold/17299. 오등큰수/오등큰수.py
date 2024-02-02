# 오등큰수

num = int(input())

row = list(map(int,input().split(' ')))

# 오등큰수를 저장하는 리스트
NGF = [-1 for i in range(num)]

# 등장 횟수를 저장하는 리스트
F = [0 for i in range(1000001)]

stack = []

# 각 숫자를 Index로 설정해서 등장 횟수 저장
for k in range(num):
    F[row[k]] += 1


for i in range(num):
    
    if not stack:
        stack.append(i)
    else:
        # stack이 빌 경우도 생각해줘야 함
        while(stack and F[row[i]] > F[row[stack[-1]]]):
            index = stack.pop()
            NGF[index] = row[i]
        stack.append(i)
        
print(*NGF)