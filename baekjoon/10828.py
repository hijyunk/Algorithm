import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    inputs = input().split()
    
    if inputs[0] == 'push':
        stack.append(int(inputs[1]))
    elif inputs[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif inputs[0] == 'size':
        print(len(stack))
    elif inputs[0] == 'empty':
        print(0 if stack else 1)
    elif inputs[0] == 'top':
        print(stack[-1] if stack else -1)