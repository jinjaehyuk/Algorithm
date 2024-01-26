import sys 
input = sys.stdin.readline
from collections import deque
n = int(input())

if n == 1:
    print(1)
    exit()
cards = [i for i in range(1,n+1)]
queue = deque(cards)
result = 0
while len(queue)>1:
    queue.popleft()
    result = queue.popleft()
    queue.append(result)
print(result)