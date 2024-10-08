L = int(input())
string = list(input())

result = 0
for i in range(len(string)):
    n = ord(string[i]) - 96
    result += n*31**i

print(result%1234567891)