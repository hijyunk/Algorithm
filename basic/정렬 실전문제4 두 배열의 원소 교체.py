n, k = map(int, input().split())
# n개 원소, k번 바꿔치기 연산

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k):
    if min(a) < max(b):
        a[a.index(min(a))] = max(b)
        b.remove(max(b))
    else:
        break
        
print(sum(a))