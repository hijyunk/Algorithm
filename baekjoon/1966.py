from collections import deque
import sys
input = sys.stdin.readline

def print_count(queue, M):
    count = 0    # 인쇄 순서

    while queue:
        if queue[0][1] == max(queue, key=lambda x:x[1])[1]:
            count += 1
            if queue[0][0] == M:
                return count
            queue.popleft()
        else:
            queue.append(queue.popleft())

n = int(input().rstrip())

for _ in range(n):
    N, M = map(int, input().rstrip().split())
    temp = list(map(int, input().rstrip().split()))
    queue = deque((idx, rank) for idx, rank in enumerate(temp))
    print(print_count(queue, M))