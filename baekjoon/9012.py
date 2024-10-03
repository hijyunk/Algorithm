T = int(input())

for _ in range(T):
    string = input()
    stack = []    # 여는 괄호 ( 를 저장하는 역할
    is_valid = True    # 문자열이 유효한지 여부

    for char in string:
        # 여는 괄호일 때
        if char == '(':
            stack.append(char)
        
        # 닫는 괄호일 때
        elif char == ')':
            # 스택이 비어있지 않다면 = 그 전에 여는 괄호가 있을 경우
            if stack:
                stack.pop()    # 닫는 괄호, 여는 괄호 짝맞추기
            # 스택이 비어 있다면 = 그 전에 여는 괄호가 없을 경우 = 애초에 닫는 괄호로 문자열이 시작한 것
            else:
                is_valid = False    # 문자열이 유효하지 않음
                break
    
    # 문자열에 문자 하나씩 조회가 끝난 후에도 스택에 여는 괄호가 있을 경우
    # = 짝이 안맞음 = 문자열이 유효하지 않음
    if stack: is_valid = False

    # 마지막으로 문자열이 유효한지 확인하고 그에 따라 출력
    if is_valid: print('YES')
    else: print('NO')