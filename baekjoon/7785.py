import sys
input = sys.stdin.readline

n = int(input())

people = set()
for _ in range(n):
    name, record = input().split()
    if record == 'enter':
        people.add(name)
    else:
        people.remove(name)

sorted_people = sorted(people, reverse=True)
print(*sorted_people, sep='\n')