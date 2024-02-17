# 진법 변환
# 알파벳을 통해서 들어오는 진법은 아스키코드에 맞춰서 설정 -> A는 65 Z는 90

# N은 입력 수 , B는 N의 진법
N, B = input().split()

# 알파벳일경우를 위해서 리스트에 저장
number = list(N)

number.reverse()

result = 0
# 10진수로 변환
for idx, val in enumerate(number):
    
    if(val >= 'A' and val <= 'Z'):
        result += (ord(val)- 55) * (int(B)**idx)
    else:
        result += int(val) * (int(B)**idx)
        
print(result)