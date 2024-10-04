import sys
input = sys.stdin.readline

N = int(input().strip())

people = []
for _ in range(N):
    x, y = map(int, input().strip().split()) # 몸무게, 키
    people.append((x,y))

rank_list = []
for i in range(N):
    rank = 0
    target_x, target_y = people[i][0], people[i][1]
    for j in range(N):
        comp_x, comp_y = people[j][0], people[j][1]
        if target_x < comp_x and target_y < comp_y:
            rank += 1
    rank_list.append(rank+1)

print(*rank_list)