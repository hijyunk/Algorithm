# 실전 문제 2. 부품 찾기 : 집합 자료형

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

arr = set(arr)

ans = ['yes' if i in arr else 'no' for i in x]
print(*ans)