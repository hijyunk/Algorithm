n = int(input())
scores = [input().split() for _ in range(n)]

scores.sort(key = lambda x: int(x[1]), reverse=True)
print(*[i[0] for i in scores])