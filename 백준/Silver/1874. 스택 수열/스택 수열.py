# 1874번 -> 스택수열
import sys

num = int(sys.stdin.readline())

# 입력받은 수열을 저장할 리스트
answer = []

# 1~n까지의 원소를 추가,삭제할 stack기능을 하는 list생성
stack = []

# NO를 판단할 수 있도록 해주는 flag (flag = 1 (True) flag = 0 (False))
flag = 1

# stack에서 가장 위(top)에 있는 수
curr = 1

# 수열 입력
for i in range(num):

    inp = int(sys.stdin.readline())

    # 스택 구조를 이용
    while curr <= inp:
        stack.append(curr)
        answer.append('+')
        curr += 1
        
    if stack[-1] == inp:
        stack.pop()
        answer.append('-')
    else:
        flag = 0


if(flag == 1):
    for val in answer:
        print(val)
else:
    print('NO')
    
    
    

    
    
    