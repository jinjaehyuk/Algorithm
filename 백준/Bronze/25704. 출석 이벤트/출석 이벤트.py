N = int(input())
P = int(input())
l = []
l.append(P)

if N >= 5:
    if 500 < P: 
        l.append(P-500)
    else:
        l.append(0)

if N>= 10:
    l.append(int(P*0.9))
if N>=15:
    if 2000 < P:
        l.append(P-2000)
    else:
        l.append(0)
if N>= 20:
    l.append(int(P * 0.75))


l.sort()
print(l[0])