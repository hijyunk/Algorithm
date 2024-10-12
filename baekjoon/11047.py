import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
A = [int(input().rstrip()) for _ in range(N)]
A = sorted(A, reverse=True)

cnt = 0
for coin in A:
    if K == 0: break
    cnt += K//coin
    K = K%coin

print(cnt)