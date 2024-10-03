M, N = map(int, input().split())

def sieve(limit):
    is_prime = [True] * (limit+1)
    is_prime[0] = is_prime[1] = False # 0,1은 소수x => False

    # 2부터 루트 N까지 소수 구하기
    for i in range(2, int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False
    
    for i in range(M, N+1):
        if is_prime[i]: print(i)

sieve(N)