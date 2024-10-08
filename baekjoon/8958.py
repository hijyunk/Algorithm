import sys
input = sys.stdin.readline

def calc(string):
    result = 0
    temp = 0
    for s in string:
        if s == 'O':
            temp += 1
            result += temp
        else:
            temp = 0
    return result

n = int(input().rstrip())
for _ in range(n):
    case = input().rstrip()
    print(calc(case))