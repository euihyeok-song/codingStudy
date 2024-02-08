# 접미사 배열
# sorted함수 사용 
# sorted함수의 원리를 잘 이해해야 함
# => 파이썬에서 sorted함수는 

word = list(input())

suffix = []

for i in range(len(word)):
    suffix.append(word[i:])

sort_suffix = sorted(suffix)

for val in sort_suffix:
    print(''.join(val))