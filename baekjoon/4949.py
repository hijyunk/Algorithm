import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '.': break

    stack = []
    for s in line:
        if s == '(': 
            stack.append('(')
        elif s == '[': 
            stack.append('[')
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        print('no' if stack else 'yes')