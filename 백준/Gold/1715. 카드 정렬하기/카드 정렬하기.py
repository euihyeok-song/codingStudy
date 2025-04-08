# 문제의 핵심 -> 계속해서 가장 작은 2개를 뽑아야 함 (우선순위 큐)
import heapq
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())
card = []
total = 0

for i in range(N):
    heappush(card,int(input()))

while len(card) > 1:
    
    first = heappop(card)
    second = heappop(card)
    
    sum_card = first + second
    
    total += sum_card
    heappush(card,sum_card)

print(total)