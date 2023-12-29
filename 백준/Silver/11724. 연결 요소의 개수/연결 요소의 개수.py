import sys
input = sys.stdin.readline
# from collections import deque

# def bfs(start):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True

# n,m = map(int,input().split())
# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     x,y = map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# count = 0
# for i in range(1, n+1):
#     if not visited[i]:
#         bfs(i)
#         count += 1 
# print(count)


sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n,m = map(int,input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
count = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1  
print(count)