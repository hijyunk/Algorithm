n = int(input())
numbers = []
for _ in range(n):
    i = int(input())
    numbers.append(i)
    
# 인덱스로 풀기
temp = [0] * max(numbers)
for i in range(n):
    temp[numbers[i]-1] += 1
print(temp.index(max(temp))+1)