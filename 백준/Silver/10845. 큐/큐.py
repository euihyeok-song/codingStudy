# Queue를 이용한 문제 (FIFO) -> 삽입은 뒤로/ 삭제는 앞으로

import sys

num = int(sys.stdin.readline().rstrip('\n'))

queue = []

for _ in range(num):
    
    command = list((sys.stdin.readline().rstrip('\n')).split())
    # print(command.__class__) -> type을 알아보는 커멘드
    
    if(command[0] == 'push'):
        queue.append(command[-1])
        
    elif(command[0] == 'pop'):
        if not queue:
            print(-1)
        else:
        # reverse -> pop -> reverse를 이용해서 맨 앞의 원소를 제거
            queue.reverse()
            print(queue.pop())
            queue.reverse()
            
    elif(command[0] == 'size'):
        print(len(queue))
        
    elif(command[0] == 'empty'):
        if queue:
            print(0)
        else:
            print(1)
            
    elif(command[0] == 'front'):
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    # command[0] == 'back'
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
        
    

