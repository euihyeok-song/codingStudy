from collections import deque

M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(layer)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
days = -1
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                queue.append((h, n, m, 0))

while queue:
    z, y, x, day = queue.popleft()
    days = max(days, day)
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomatoes[nz][ny][nx] == 0:
            tomatoes[nz][ny][nx] = 1
            queue.append((nz, ny, nx, day + 1))

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 0:
                print(-1)
                exit()

print(days)
