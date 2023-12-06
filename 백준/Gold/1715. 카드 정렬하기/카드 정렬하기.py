import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
for i in range(N):
    heapq.heappush(heap,int(input()))

result = 0
for i in range(N-1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a+b
    heapq.heappush(heap,a+b)
print(result)