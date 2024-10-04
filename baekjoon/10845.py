import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    orders = input().split()

    if orders[0] == 'push':
        stack.append(int(orders[1]))
    elif orders[0] == 'pop':
        print(stack.pop(0) if stack else -1)
    elif orders[0] == 'size':
        print(len(stack))
    elif orders[0] == 'empty':
        print(0 if stack else 1)
    elif orders[0] == 'front':
        print(stack[0] if stack else -1)
    elif orders[0] == 'back':
        print(stack[-1] if stack else -1)