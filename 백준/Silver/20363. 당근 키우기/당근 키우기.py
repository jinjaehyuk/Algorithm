import sys
input = sys.stdin.readline

a =  list(map(int,input().split()))    
a.sort()
X = a[1]
Y = a[0]
sum = X + Y + (Y //10)
print(sum)