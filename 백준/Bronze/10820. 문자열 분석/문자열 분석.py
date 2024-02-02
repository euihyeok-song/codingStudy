# 문자열 분석
# 테스트 케이스 갯수가 지정되지 않았음으로, 입력되지 않거나, 오류가 발생하기 전까지는 계속 입력을 받도록 설정

while True:
    
    try:
        sentence = list(input())

        # 1번쨰 칸 = 소문자 / 2번쩨 칸 = 대문자/ 3번째 칸 = 숫자 / 4번째 칸 = 공백
        count = [0 for i in range(4)]

        for val in sentence:
            # val.islower() == True(val이 소문자면)
            if(val.islower()):
                count[0] += 1
            elif(val.isupper()):
                count[1] += 1
            elif(val.isdigit()):
                count[2] += 1
            elif(val.isspace()):
                count[3] += 1
                
        print(*count)
    
    except EOFError:
        break