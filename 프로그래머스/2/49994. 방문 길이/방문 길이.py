def solution(dirs):
    
    x, y, cnt = 0, 0, 0
    moved_path = set()
    
    command = {"U": [0,-1], "D": [0,1], "R": [1,0], "L": [-1,0]}
    
    for val in dirs:
        nx, ny = x + command[val][0], y + command[val][1]
        if -5 <= nx < 6 and -5 <= ny < 6:
            # 양방향으로 탐지
            moved_path.add(((x, y), (nx, ny)))
            moved_path.add(((nx, ny), (x, y)))
            x, y = nx, ny
    
    return len(moved_path)//2