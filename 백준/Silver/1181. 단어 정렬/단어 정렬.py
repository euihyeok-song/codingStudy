import sys

input = sys.stdin.readline

N = int(input().strip())
words = set(input().strip() for _ in range(N))

sorted_words = sorted(words, key=lambda x: (len(x), x))

print("\n".join(sorted_words))
