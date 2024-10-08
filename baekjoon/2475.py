nums = list(map(int, input().split()))
print(sum([num**2 for num in nums]) % 10)