import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

name = {}
idx = {}
for i in range(N):
    poke = input().rstrip()
    name[poke] = i
    idx[i] = poke

for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(idx[int(q)-1])
    else:
        print(name[q]+1)