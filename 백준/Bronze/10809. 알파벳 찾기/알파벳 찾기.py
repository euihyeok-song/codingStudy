# 알파벳 찾기

word = list(input())

# a부터 z까지의 총 갯수는 26개
num = [-1 for i in range(26)]

for idx,val in enumerate(word):
    
    index = ord(val)-ord('a')
    # 중복되는 알파벳 발생시 처음으로 나온 index를 출력하기 위한 조건ㄴ
    if(num[index] == -1):
        num[index] = idx
    else:
        continue
    
print(*num)