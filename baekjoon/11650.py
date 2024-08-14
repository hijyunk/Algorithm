import sys
input = sys.stdin.readline

n = int(input())

coord = []

for _ in range(n):
    x, y = input().split()
    coord.append([int(x), int(y)])

coord = sorted(coord, key=lambda x : (x[0],x[1]))

for i in range(n):
    print(coord[i][0], coord[i][1])