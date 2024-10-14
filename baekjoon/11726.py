# 2xn 직사각형
n = int(input())

if n == 1: 
    print(1)
elif n == 2:
    print(2)
else:
    prev1 = 1
    prev2 = 2

    for _ in range(3, n+1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    
    print(prev2 % 10007)