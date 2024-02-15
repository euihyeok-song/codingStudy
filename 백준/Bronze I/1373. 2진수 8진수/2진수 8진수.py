# 2진수 8진수
# 파이썬은 2진수,8진수,16진수로 바꾸는 내장함수를 가지고 있다
# 2진수 - bin(), 8진수 - oct() , 16진수 - hex()
# 진수 관련 내용 = https://www.daleseo.com/python-int-bases/

number = input()

binary = int(number,2)

octimal = oct(binary)

print(octimal[2:])