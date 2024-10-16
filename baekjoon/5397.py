t = int(input())

for _ in range(t):
    L = input()

    left = []
    right = []
    for l in L:
        if l == '-':
            if left:
                left.pop()
        elif l == '<':
            if left:
                right.append(left.pop())
        elif l == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(l)
    print(*left + list(reversed(right)), sep='')