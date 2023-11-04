N = int(input())    

t = list(map(int,input().split()))

t.sort(reverse=True)
a=[]
for i  in range(len(t)):
    a.append(t[i]+i+1)

print(max(a)+1)