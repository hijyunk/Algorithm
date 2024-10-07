import sys
input = sys.stdin.readline

N = int(input().rstrip())
num_list = [int(input().rstrip()) for _ in range(N)]

# 1: 산술평균 (소수점 첫째 자리에서 반올림)
print(round(sum(num_list) / len(num_list)))

# 2: 중앙값
sorted_list = sorted(num_list)
print(sorted_list[N//2])

# 3: 최빈값 (여러 개 > 2번째 작은 값)
cnt = [0] * 8001    # 정수 범위 = -4000 ~ 4000
for num in num_list: 
    cnt[num+4000] += 1    # -4000을 0으로 둬서 num+4000을 함

max_freq = max(cnt)    # 최대 빈도수
modes = [i-4000 for i, freq in enumerate(cnt) if freq == max_freq]

if len(modes) > 1:    # 최빈값이 여러개면
    mode = sorted(modes)[1]    # 두번째로 작은 값
else:
    mode = modes[0]

print(mode)

# 4: 범위
print(abs(max(num_list) - min(num_list)))