import sys
import math
input = sys.stdin.readline

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:		
            return False
    return True			

n = int(input())

number = list(map(int,input().split()))

count = 0
for i in number:
    if i == 1:
        count -=1
    if primenumber(i):
        count += 1
print(count)
