N = int(input())
P = list(map(int, input().split()))
P = sorted(P)

result = 0
now = 0

for p in P:
    now += p
    result += now

print(result)