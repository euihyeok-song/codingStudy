from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

members = list(range(n))
min_diff = float('inf')

for team in combinations(members, n // 2):
    start_team = list(team)
    link_team = list(set(members) - set(start_team))

    start_score = 0
    link_score = 0

    for i in range(n // 2):
        for j in range(n // 2):
            if i != j:
                start_score += s[start_team[i]][start_team[j]]
                link_score += s[link_team[i]][link_team[j]]

    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)
