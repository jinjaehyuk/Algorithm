import sys 
input = sys.stdin.readline
from collections import deque



def bfs():
    queue = deque()
    queue.append((home_x,home_y))
    while queue:
        x, y = queue.popleft()
        if abs(festival_x - x) + abs(festival_y - y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                new_x , new_y = graph[i]
                if abs(new_x - x) + abs(new_y-y) <= 1000:
                    visited[i] =1
                    queue.append((new_x,new_y))
    print("sad")
    return
        
t = int(input())
for _ in range(t):
    n = int(input())
    home_x , home_y = map(int,input().split())
    graph = []
    for _ in range(n):
        store_x, store_y = map(int,input().split())
        graph.append((store_x,store_y))
    festival_x,festival_y = map(int,input().split())
    visited = [0 for _ in range(n+1)]
    bfs()