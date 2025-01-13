# a부터 z까지 총 26개
num = [0] * 26

word = list(input())

# 'a'의 아스키코드는 97
for val in word:
    num[ord(val)-97] += 1
    
for j in num:
    print(j, end=' ')



