n = int(input())
order = []
for _ in range(n):
    age, name = input().split()
    order.append((int(age), name))
    
sorted_order = sorted(order, key=lambda x: x[0], reverse=True)
print(*[i[1] for i in sorted_order], sep='\n')