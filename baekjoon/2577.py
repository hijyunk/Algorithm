A = int(input())
B = int(input())
C = int(input())

mul = A*B*C

for i in range(10):
    count = 0
    for j in str(mul):
        if str(i) == j:
            count += 1
    print(count)