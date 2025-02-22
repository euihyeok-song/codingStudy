from collections import deque

def solution():
    t = int(input())
    
    for _ in range(t):
        l = int(input())
        current_x, current_y = map(int, input().split())
        target_x, target_y = map(int, input().split())
        
        if current_x == target_x and current_y == target_y:
            print(0)
            continue
            
        board = [[-1] * l for _ in range(l)]
        moves = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
        
        q = deque()
        q.append((current_x, current_y))
        board[current_x][current_y] = 0
        
        while q:
            x, y = q.popleft()
            
            if x == target_x and y == target_y:
                print(board[x][y])
                break
                
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == -1:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1

solution()