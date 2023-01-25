count = int(input())

i = 0;
AA =[]
BB = []
for i in range(count):
    A, B = map(int, input().split())
    AA.append(A)
    BB.append(B)

for i in range(count):
    print('Case #%d: %d' %(i+1,AA[i]+BB[i]))