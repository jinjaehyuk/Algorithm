import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,-x)