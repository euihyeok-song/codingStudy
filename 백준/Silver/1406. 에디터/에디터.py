import sys
from collections import deque

input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()

M = int(input())

result = ''

for _ in range(M):

    command = input().rstrip()
    
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[2])
        
# 시간 단축을 위해 extend() 사용
reversedRight = reversed(right)
left.extend(reversedRight)

print(''.join(left))