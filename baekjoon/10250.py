import sys
input = sys.stdin.readline

def hotel(H, N):
    room = N // H + 1
    floor = N % H

    if floor == 0: # 마지막 층
        floor = H
        room -= 1
    return f"{floor}{room:02}"

T = int(input().rstrip())

for _ in range(T):
    H, W, N = map(int, input().rstrip().split())
    print(hotel(H, N))