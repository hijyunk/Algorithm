T = int(input())

dp = [[0] * 15 for _ in range(15)] # 최대 14층, 14호

# 0층에는 n명이 산다
for i in range(1, 15):
    dp[0][i] = i

for f in range(1, 15): # 1~14층
    for ho in range(1, 15): # 1~14호
        dp[f][ho] = dp[f][ho-1] + dp[f-1][ho]

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    print(dp[k][n])