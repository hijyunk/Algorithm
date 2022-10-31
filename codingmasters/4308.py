n = int(input())

flag = 0

for i in range(2, int(n**0.5) + 1):
    if n % i == 0: flag += 1

if flag == 0 and n != 1: print(1)
else: print(0)