import sys
input = sys.stdin.readline


N = list(input().strip())

N.sort(reverse=True)
s = int(''.join(N))
if s%30 ==0:
    print(s)
else:
    print(-1)