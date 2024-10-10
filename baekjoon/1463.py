N = int(input())

def one(N):
    dp = [0] * (N+1)    # 횟수 저장하는 테이블
    # dp[1]은 이미 1이기 때문에 dp[1]=0

    for i in range(2, N+1):
        # 1 빼기 = 그 전 숫자의 횟수 + 1
        dp[i] = dp[i-1] + 1

        # 2로 나누어지면
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)    # '1 빼기'와 비교를 해서 횟수 적은 값 고르기
        
        # 3으로 나누어지면
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)    # '1 빼기'와 비교를 해서 횟수 적은 값 고르기
    
    return dp[N]

print(one(N))