import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

def count_lines(lines, length):
    cnt = 0
    for line in lines:
        cnt += line // length
    return cnt

def calc_length(lines, N):
    low = 1    # 랜선 길이 최소값
    high = max(lines)    # 랜선 길이 최대값
    result = 0

    while low <= high:
        mid = (low + high) // 2    # 중간값

        # 만든 랜선 개수가 필요한 랜선 개수보다 크거나 같을 때
        if count_lines(lines, mid) >= N: 
            result = mid    # 더 긴 랜선을 만들 수 있으니 결과를 저장
            low = mid + 1    # 더 긴 길이도 가능한지 확인

        # 만든 랜선 개수가 필요한 랜선 개수보다 적을 때
        else:
            high = mid - 1    # 길이를 더 줄인다
    
    return result

print(calc_length(lines, N))