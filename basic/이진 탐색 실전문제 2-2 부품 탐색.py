# 실전 문제 2. 부품 찾기 : 계수 정렬

# N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1
    
# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
ans = ['yes' if array[i] != 0 else 'no' for i in x]
print(*ans)