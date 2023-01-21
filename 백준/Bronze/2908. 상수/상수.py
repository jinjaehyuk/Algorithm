A,B =  input().split()

A_l = list(A)
B_l = list(B)

re_A_l = []
re_B_l = []
for i in range(2, -1, -1):
    re_A_l.append(A_l[i])
    re_B_l.append(B_l[i])

if int(('').join(re_A_l)) > int(('').join(re_B_l)) :
    print(int(('').join(re_A_l)))
else:
    print(int(('').join(re_B_l)))