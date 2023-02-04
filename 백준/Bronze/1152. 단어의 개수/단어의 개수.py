A = input()
B = A.split(" ")
if(B[0]==''):
    B.remove(B[0])
if B[len(B)-1] == '':
    B.remove(B[len(B)-1])
print(len(B))