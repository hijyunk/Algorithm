n = int(input())

users = []
for _ in range(n):
    age, user = input().split()
    users.append((int(age), user))

users = sorted(users, key=lambda x: x[0])
for i in range(n):
    print(users[i][0], users[i][1])