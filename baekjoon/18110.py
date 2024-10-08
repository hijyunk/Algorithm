import sys
input = sys.stdin.readline

def custom_round(value):
    return int(value+0.5)

n = int(input().rstrip())

if n == 0:
    print(0)
else:
    n_list = [int(input().rstrip()) for _ in range(n)]
    n_list = sorted(n_list)
    ex = custom_round(n*0.15)
    if ex > 0:
        n_list = n_list[ex:-ex]
    print(custom_round(sum(n_list)/len(n_list)))