N = input()
N = N.zfill(2)

cnt = 0
sum = 0
while True:
    if cnt == 0:
        A = int(N[0:1])
        B = int(N[1:2])
    else:
        A = int(N1[0:1])
        B = int(N1[1:2])
    sum = A+B
    sum = str(sum).zfill(2)
    new_num =int(str(B) + sum[1:2]) 
    
    cnt = cnt+1
    if(int(N) == new_num):
        print(cnt)
        break
    else:
        N1 = str(new_num)
        N1 = N1.zfill(2)
        