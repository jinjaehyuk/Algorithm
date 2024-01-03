import sys
input = sys.stdin.readline
from collections import deque

T = int(input())


def dfs(v):
    visited[v] = True
    global count
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
for _ in range(T):
    a = []
    a_temp = []
    n = int(input())
    a = list(map(int,input().split()))    
    a_temp = sorted(a)
    graph = [[] for  _ in range(n+1)]
    for i in range(n):
        x, y = a_temp[i], a[i]
        graph[x].append(y)
        graph[y].append(x)
            
    visited = [False]* (n+1)
    
    count = -1
    
    for i in range(n+1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)
    
    