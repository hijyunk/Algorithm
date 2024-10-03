T = int(input())

def replace(string):
    if '()' in string:
        string = string.replace('()', '')
        return replace(string)
    else:
        return string

for _ in range(T):
    string = input()
    result = replace(string)
    if len(result) == 0:
        print('YES')
    else:
        print('NO')