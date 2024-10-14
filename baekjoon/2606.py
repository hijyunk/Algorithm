import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a][b], graph[b][a] = 1, 1

visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    for i in range(1, n+1):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i)
dfs(1)

print(sum(visited)-1)