import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    answer = input().rstrip()
    left = []
    right = []
    
    for i in answer:
        
        if i == '<' and left:
            right.append(left.pop())
        elif i == '>' and right:
            left.append(right.pop())
        elif i == '-' and left:
            left.pop()
        elif 48 <= ord(i) <= 57 or 65 <= ord(i) <= 122:
            left.append(i)
    
    total = left + list(reversed(right))
    
    print(''.join(total))