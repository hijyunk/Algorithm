n = int(input())
arr = list(map(int, [input() for _ in range(n)]))

arr = sorted(arr, reverse=True)
print(*arr, sep=' ')