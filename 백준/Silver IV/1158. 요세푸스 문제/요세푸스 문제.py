# 순열문제
# 1. 리스트에 1~N까지 저장해주고, 제거된 수는 pop시켜서 리스트 내부의 원소가 하나도 없으면 끝
# 2. circular linkedlist로 풀기 가능 -> 삭제만 필요
    
## 런타임 에러 발생 ->  인덱스 오류/ 0으로 나누기 오류/ 변수의 정의 오류/ 타입 오류 등과 같은 코드의 문제
#               ->  배열 인덱스 참조의 가능성이 가장 큼                
    

# solution -> %(나머지연산 사용)


N, K = map(int,input().split(' '))

circle = [i+1 for i in range(N)]

delete = []

idx = 0

for i in range(N):
    
    idx += K-1
    
    # 가장 마지막 index
    end = len(circle)-1
    
    # 현재 리스트의 길이
    length = len(circle)
    
    while(idx > end):
        idx -= length
        if(idx <= end):
            break
        
    if(length == 1):
        idx = 0
        
    delete.append(circle.pop(idx))
    
print("<",end='')
    
for j in range(len(delete)):
    
    if(j < len(delete)-1):
        print(delete[j],end=', ')
    else:
        print(delete[j],end='')
    
print(">")
    