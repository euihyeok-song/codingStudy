import sys
from collections import Counter

input = sys.stdin.readline

first = Counter(input().rstrip())
second = Counter(input().rstrip())

total = (first-second) + (second-first)

print(sum(total.values()))