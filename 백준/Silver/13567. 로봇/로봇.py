# TURN 0: 왼쪽 90도 회전 / TURN 1: 오른쪽으로 90도 회전 / MOVE d: 해당 방형으로 d이동
# 처음에는 오른쪽을 보고 있다.

M, N = map(int, input().split(' '))
# 1: 서, 2: 북, 3: 동, 4:남
direction = 3
curr = [0,0]

for _ in range(N):
    
    command = list(input().split(' '))

    if command[0] == 'MOVE':
        if direction == 1:
            curr = [curr[0] - int(command[1]) , curr[1]]
        elif direction == 2:
            curr = [curr[0], curr[1] + int(command[1])]
        elif direction == 3:
            curr = [curr[0] + int(command[1]) , curr[1]]
        else: 
            curr = [curr[0], curr[1] - int(command[1])]
    else:
        if command[1] == '1':
            direction += 1
            
            # 남 -> 서 일경우 에는 서에 맞게 수정
            if direction == 5:
                direction = 1
        else:
            direction -= 1
            
            # 서 -> 남 일경우 에는 남에 맞게 수정
            if direction == 0:
                direction = 4
                
    if curr[0] < 0 or curr[1] < 0 or curr[0] > M or curr[1] > M:
        print(-1)
        exit()

print(curr[0], curr[1])