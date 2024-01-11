# 파이썬에서 list는 삽입시 insert함수 사용 X / 삭제시 del함수 사용 X -> time complexity O(N)
# 1. pop함수와 append함수를 이용
# 2. stack구조를 이용
# 3. pointer을 가진 LinkedList를 통해서 풀수도 있음

# pop 함수는 pop시킬 위치 지정가능 -> pop(1)-> 1번째 index의 값을 삭제 -> default값이 -1이므로, list.pop()을 하면 가장 뒤에 원소가 사라짐

import sys

# readline함수를 통해 읽어온 입력은 default가 string임
input_str = sys.stdin.readline().rstrip('\n')

# list함수를 통해 문자열이 문자로 분리되서 저장됨
lstack = list(input_str.lower())

# command를 수행할 횟수
num = int(sys.stdin.readline())

# 문자열의 길이와 커서의 현재 위치를 보면서 하는 것이 아닌 stack을 2개 선언함을 통해 해결
# rstack의 가장 top부분은 현재 커서가 가르키는 부분
rstack = []

for i in range(num):

    # command는 L, D, B, P ~ => 총 4개가 존재
    # readline 함수를 이용해서 읽어올 때는 항상 개행문자('\ㅜ')가 붙으니 제거해줌
    command = sys.stdin.readline().rstrip('\n')
    
    if(command == 'L'):
        # lstack이 비어있지 않을때 -> if lstack is not empty
        if lstack:
            rstack.append(lstack.pop())
            
    elif(command == 'D'):
        if rstack:
            lstack.append(rstack.pop())
            
    elif(command == 'B'):
        if lstack:
            lstack.pop()
        
    # command가 P ~ 인경우    
    else:
        store = command.split()
        lstack.append(command[-1])
        

# reverse함수 -> 리스트를 뒤집으며, return값이 없음 -> list.reverse() -> reverse함수는 tuple/dict/str은 지원 불가
# reverse함수는 리스트가 비어있으면 error를 발생시킨
# reversed함수 -> 리스트를 뒤집으며, 뒤집은 리스트의 값을 return -> reversed(list) -> dict만 제외하고 모두 지원

reverse_stack = reversed(rstack)
lstack.extend(reverse_stack)

# array배열은 char형식이므로, join함수를 이용해서 문자열로 바꿔 출력
print(''.join(lstack[:]))

    