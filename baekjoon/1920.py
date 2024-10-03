import sys
input = sys.stdin.readline

N = int(input())
A = set(list(map(int, input().split())))

M = int(input())
M_list = list(map(int, input().split()))

for m in M_list:
    print(1 if m in A else 0)