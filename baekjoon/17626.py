import math

n = int(input())

def square(n):
    # 제곱수 1개
    if int(math.sqrt(n))**2 == n:
        return 1
    
    # 제곱수 2개
    for i in range(1, int(math.sqrt(n))+1):
        # n-i^2를 제곱근하고 제곱 = n-i^2이면 n은 제곱수 2개로 이루어져있다.
        if int(math.sqrt(n - i**2))**2 == (n - i**2):
            return 2
    
    # 제곱수 3개
    while n % 4 == 0:    # 4의 배수 제외
        n //= 4
    if n % 8 == 7:    # 8로 나눴을 때 나머지가 7이면 반드시 4개의 제곱수
        return 4
    
    return 3

print(square(n))