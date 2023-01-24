T = int(input())
sum_l = []
for i in range(T):
    A,B = map(int,input().split())
    sum_l.append(A+B)

for i in range(len(sum_l)):
    print(sum_l[i])
   
         