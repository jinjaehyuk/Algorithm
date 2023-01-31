n = []
m = list(range(1,31))
for i in range(0,28,1):
    n.append(int(input()))

for i in range(0,len(n),1):
    for j in range(0,len(m),1):
            if n[i] == m[j] :
                m.remove(m[j])
                break

m = sorted(m)
print(m[0])
print(m[1])