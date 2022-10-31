n = int(input())
k = list(map(int, input().split()))
k = sorted(k)

answer = 0
for i in range(n):
    power = min(k[i:])*len(k[i:])
    if answer <= power: answer = power
print(answer)