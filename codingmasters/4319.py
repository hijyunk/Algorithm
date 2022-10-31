n = int(input())
numbers = []
for _ in range(n):
    k = int(input())
    numbers.append(k)
    
temp = [0] * max(numbers)
for i in range(n):
    temp[numbers[i]-1] += 1   

max_stock = list(filter(lambda x: temp[x] == max(temp), range(len(temp))))
print(max_stock[-1]+1)