# 알파벳 개수

word = list(input())

# 소문자 a부터 z까지의 총 갯수는 26개
number = [0 for i in range(26)]

for val in word:
    
    index = ord(val) - ord('a')
    number[index] += 1

print(*number)