import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

n = {input().rstrip() for _ in range(N)}
m = {input().rstrip() for _ in range(M)}
nm = n&m

print(len(nm))
print(*sorted(nm), sep='\n')