n, m = map(int, input().split())
p = list(map(int, input().split))
p = sorted(p, reverse=True)

temp = 0
cnt = 0
for i in range(m):
    if temp+p[i] > n: 
        continue
    else:
        temp += p[i]
        cnt += 1

print(cnt)