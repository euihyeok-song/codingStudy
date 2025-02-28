# dict 이용
import sys

input = sys.stdin.readline

N = int(input())
card = list(input().rstrip().split(' '))
M = int(input())
cnt = list(input().rstrip().split(' '))

dictionary = dict()

for i in card:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(*[dictionary[j] if j in dictionary else '0' for j in cnt])

