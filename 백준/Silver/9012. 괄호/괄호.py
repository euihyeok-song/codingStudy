# 괄호

# python에서는 range보다는 enumerate함수를 많이 씀
# 1. range함수는 len함수와 함께 쓰여야 함 2. range는 리스트의 인덱스로만 접근이 가능  -> enumerate함수가 좀 더 pythonic한 함수여서 enumerate함수를 자주 사용
# enumerate함수는 1,2를 모두 해결해줌 + enumerate는 idx과 result를 함께 출력가능 / enumerate는 enumerate(fruits,1) -> 시작인덱스를 지정가능

# readline을 쓰기위한 라이브러리
import sys

times = int(sys.stdin.readline().rstrip('\n'))

for i in range(times):
    # num1, num2 = 0, 0  -> '(', ')'의 총갯수를 통해서 확인해보려 햇지만 예외가 발생하여 보류

    flag = 0
    
    stack = []
    
    sentence = list(map(str,sys.stdin.readline().rstrip('\n')))

    for _,val in enumerate(sentence):
        if(val == '('):
            stack.append('(')
        else:
            if not stack:
                flag = 1
                break
            else:
                stack.pop()
    
    if(flag == 0):
        if not stack:
            print('YES')
        else:
            print('NO')
          
    else:
        print('NO')
    