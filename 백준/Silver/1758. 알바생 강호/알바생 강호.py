import sys
input = sys.stdin.readline

N = int(input())

tip = []
for _ in range(N):
    tip.append(int(input()))

tip.sort(reverse=True)

result = 0

for i in range(N):
    sum = 0
    sum = tip[i]-((i+1)-1)
    if sum < 0:
        break
    result += sum
print(result)