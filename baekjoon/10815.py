import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

mat_plus = [0]*10000001
mat_minus = [0]*10000001

for i in cards:
    if i >= 0: mat_plus[i] += 1
    else: mat_minus[-i] += 1
    
m = int(input())
check = list(map(int, input().split()))

for i in check:
    if i >= 0:
        print(mat_plus[i], end=' ')
    else:
        print(mat_minus[-i], end=' ')