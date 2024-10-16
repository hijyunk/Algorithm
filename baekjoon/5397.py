from collections import deque

t = int(input())

for _ in range(t):
    L = input()

    left = deque()
    right = deque()

    for l in L:
        if l == '-':
            if left:
                left.pop()
        elif l == '<':
            if left:
                right.appendleft(left.pop())
        elif l == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(l)
    print(*left + right, sep='')