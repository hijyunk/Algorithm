N, K = map(int, input().split())

a = list(range(N-K+1, N+1))
b = list(range(2, K+1))

def multiply(list):
    result = 1
    for num in list:
        result *= num
    return result

print(int(multiply(a)/multiply(b)))