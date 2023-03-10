n = int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))
    
arr = sorted(arr, key = lambda arr: arr[1])
print(*[arr[i][0] for i in range(len(arr))])