import sys
from collections import deque

input = sys.stdin.readline

T  = int(input())

for _ in range(T):
    
    func = deque(input().rstrip())
    num = int(input())
    # num에 0이오면 무시할 수 있도록 설정
    dq = deque(map(int,input()[1:-2].split(','))) if num > 0 else deque(input()[1:-2])
    
    flag = 0
    # reverse 여부로, 뒤집히면 flag가 바뀐다 ( 정상: 1, 반대: -1 )
    rflag = 1

    while func:
        
        if func[0] == 'R':
            if dq:
                rflag *= -1
        elif func[0] == 'D' and rflag == 1:
            if dq:
                dq.popleft()
            else:
                flag = 1
                break
        elif func[0] == 'D' and rflag == -1:
            if dq: 
                dq.pop()
            else:
                flag = 1
                break
        
        func.popleft()
    
    if flag != 1 and rflag == 1:
        print("[",end='')
        for i in range(len(dq)):
            print(dq[i], end=',' if i != len(dq) - 1 else '')
        print("]")
    elif flag != 1 and rflag == -1:
        print("[",end='')
        for i in range(len(dq)-1,-1,-1):
            print(dq[i], end=',' if i != 0 else '')
        print("]")
    else:
        print("error")
