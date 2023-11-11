N = input()

a = "AAAA"  
b = "BB"

N =N.replace('XXXX',a)
N = N.replace('XX',b)

if 'X' in N:
    print(-1)
else:
    print(N)