n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
answer = []

current = 1 # 1부터 시작

for num in seq:
    while current <= num: # 현재 스택의 최상단 숫자가 목표 수열의 숫자보다 작다면
        stack.append(current) # push
        answer.append('+')
        current += 1 # 다음 숫자

    if stack[-1] == num: # 스택의 최상단 숫자가 현재 목표 수열의 숫자라면
        stack.pop() # pop
        answer.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(answer))