import sys
input = sys.stdin.readline

K = int(input().strip())

m = []
for _ in range(K):
    n = int(input().strip())
    if n == 0: m.pop()
    else: m.append(n)

print(sum(m))