import sys
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
a = int(input())
b = int(input())

graph = [[] for _ in range(a+1)]

for i in range(b):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (a+1)

count = -1 



dfs(1)
print(count)


