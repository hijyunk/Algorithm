import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    clothes = {}
    result = 1
    n = int(input().rstrip())
    for _ in range(n):
        name, type = input().rstrip().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    for i in clothes.values():
        result *= (i+1)
    print(result - 1)    # 알몸인 경우 제외