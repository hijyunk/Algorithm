import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

pwd_list = {}
for _ in range(N):
    addr, pwd = input().rstrip().split()
    pwd_list[addr] = pwd

for _ in range(M):
    q = input().rstrip()
    print(pwd_list.get(q))