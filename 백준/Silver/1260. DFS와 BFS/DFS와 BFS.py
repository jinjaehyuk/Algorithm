import sys
input = sys.stdin.readline
from collections import deque


n,m,v = map(int,input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)] 
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
visited_bfs = [False] * (n+1)
visited_dfs = [False] * (n+1)

def dfs(graph,v,visited_dfs):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in range(1,n+1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(graph,i,visited_dfs)

def bfs(graph,v,visited_bfs):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visited_bfs[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited_bfs[i] = True
                


dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)
