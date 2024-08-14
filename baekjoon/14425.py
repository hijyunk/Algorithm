import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
words = []
for _ in range(n):
    s.append(input())
for _ in range(m):
    words.append(input())

cnt = 0
for i in words:
    if i in s: cnt += 1
print(cnt)
