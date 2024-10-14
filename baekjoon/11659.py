import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

pre_sum = [0]
s = 0
for idx in range(N):
    s += nums[idx] 
    pre_sum.append(s)

for _ in range(M):
    i, j = map(int, input().split())
    print(pre_sum[j]-pre_sum[i-1])