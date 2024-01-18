# Deque 구현하기

import sys

num = int(sys.stdin.readline())

deqeue = []

for i in range(num):
    
    command = list(sys.stdin.readline().rstrip('\n').split())

    # command의 길이가 2인경우
    if(len(command) > 1):
        
        # command[0] 부분을 _기준으로 나눔
        new = command[0].split('_')
        
        # 앞으로 넣기 위해서 덱을 뒤집어서 append하고 다시 뒤집는 방식 사용
        if(new[0] == 'push' and new[1] == 'front'):
            deqeue.reverse()
            deqeue.append(command[1])
            deqeue.reverse()
        
        # push_back X인 경우    
        else:
            deqeue.append(command[1])
    
    # command의 길이가 1인경우
    else:
        
        if(command[0] == 'pop_front'):
            if not deqeue:
                print('-1')
            else:
                deqeue.reverse()
                ans = deqeue.pop()
                deqeue.reverse()
                print(ans)
                
        elif(command[0] == 'pop_back'):
            if not deqeue:
                print('-1')
            else:
                ans = deqeue.pop()
                print(ans)
            
        elif(command[0] == 'size'):
            print(len(deqeue))
            
        elif(command[0] == 'empty'):
            if not deqeue:
                print('1')
            else:
                print('0')
            
        elif(command[0] == 'front'):
            if not deqeue:
                print('-1')
            else:
                print(deqeue[0])
            
        # back인 경우    
        else:
            if not deqeue:
                print('-1')
            else:
                print(deqeue[-1])