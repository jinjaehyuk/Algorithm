import sys
input = sys.stdin.readline

trail = []
total = 0
for i in range(10):
    minus, plus = map(int,input().split())
    total = total - minus + plus
    trail.append(total)
print(max(trail))