import sys
input = sys.stdin.readline

N = input().strip()

r = N.split('-')
b = []
for i in range(len(r)):
    if r[i].split('+'):
        b = map(int,r[i].split('+'))
        r[i] = sum(b)
result = r[0]
for i in range(1,len(r)):
    result -= r[i]
print(result)