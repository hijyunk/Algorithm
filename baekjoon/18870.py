import sys
input = sys.stdin.readline

n = int(input())
coord = list(map(int, input().split()))
order_list = sorted(set(coord))
new_coord = {order_list[i]:i for i in range(len(order_list))}

for i in coord:
    print(new_coord[i], end=' ')