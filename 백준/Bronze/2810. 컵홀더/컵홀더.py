N = int(input())    
seat = list(input())
b = []
b.append('*')
for i in range(len(seat)):
    if seat[i] == 'S':
        b.append(seat[i])
        b.append('*')
    elif seat[i] =='L':
        if b[len(b)-1] !='L':
            b.append(seat[i])
        else:
            b.append(seat[i])
            b.append('*')

a = b.count('*')
if N > a:
    print(a)
else:
    print(N)