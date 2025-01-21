import sys
from collections import Counter

input = sys.stdin.readline

first = list(input().rstrip())
second = list(input().rstrip())

if len(first)>len(second):
    first, second = first, second

total = 0
for i in first:
    if i in second:
        second.remove(i)
        total += 1
print(len(first)-total + len(second))