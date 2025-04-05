import sys

input = sys.stdin.readline

sentence = input().split('-')
result = sum(map(int, sentence[0].split('+')))
for word in sentence[1:]:
    result -= sum(map(int, word.split('+')))
print(result)
