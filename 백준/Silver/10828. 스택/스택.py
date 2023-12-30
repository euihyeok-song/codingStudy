# 스택 => LIFO(Last in First out)
import sys                               # input함수 대신 readline을 사용하기 위한 라이브러리

stack = []

# 받을 명령의 수를 저장
times = int(sys.stdin.readline())

# 입력 받는 값을 명령 / 숫자로 나눠서 정수/문자열로 변환
for i in range(times):
    
    ans = list(map(str,sys.stdin.readline().split()))           # 한 두줄이 아닌 여러줄을 입력받을때, input함수는 시간초과 발생
                                                        # sys.stdin.readline()함수는 \n을 함께 받아옴 -> str으로 형변환 필요
    
    if(len(ans) >= 2):          # input를 구성하는 단어 수의 길이를 통해서 check    / len함수의 time complexity = O(1)
        a, b = ans[0],ans[1]            # push + 숫자 형식일때 사용
        b = int(b)                      # res값은 문자열에서 정수형으로 형변환
        
        if(a == 'push'):
            stack.append(b)
    
    else:
        if(ans[0] == 'pop'):
            if(len(stack) == 0):
                print(-1)
            else:    
                res = stack.pop()
                print(res)
                
        elif(ans[0] == 'size'):
            length = len(stack)
            print(length)
            
        elif(ans[0] == 'empty'):
            if(len(stack)==0):
                print(1)
            else:
                print(0)
                
        elif(ans[0] == 'top'):                          # ans == top인 경우
            if(len(stack)==0):
                print(-1)
            else:
                print(stack[-1])
