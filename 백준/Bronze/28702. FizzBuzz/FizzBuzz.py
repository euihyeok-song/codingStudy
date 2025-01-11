import sys

num = [sys.stdin.readline().strip() for _ in range(3)]

# 가장 마지막 숫자 찾기 
for i in range(2, -1, -1):
    
    if num[i].isdigit():
        answer = int(num[i]) + (3-i)
        break      
      
if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)