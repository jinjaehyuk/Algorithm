import sys
input = sys.stdin.readline

N = int(input())    
K = int(input())    

sen = list(map(int,input().split()))
sen.sort()

temp = []
for i in range(1,len(sen)):
    temp.append(sen[i] - sen[i-1])
    
temp.sort()

print(sum(temp[:N-K]))