def backtrack(n, m, sequence, visited):
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return

    for i in range(1, n + 1):
        if not visited[i]:  # 중복 없이 선택
            visited[i] = True
            backtrack(n, m, sequence + [i], visited)
            visited[i] = False  # 백트래킹

def solve():
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    backtrack(n, m, [], visited)

solve()
