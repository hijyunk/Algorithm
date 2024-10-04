import math

N = int(input())    # 참가자 수
size = list(map(int, input().split()))
T, P = map(int, input().split())    # 티셔츠 묶음, 펜 묶음

tshirt = 0
for i in size:
    tshirt += math.ceil(i/T)

print(tshirt)
print(N//P, N%P)