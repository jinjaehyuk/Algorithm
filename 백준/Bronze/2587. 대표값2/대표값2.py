N = []
sum = 0
for i in range(5):
    N.append(int(input()))
    sum += N[i]
N = sorted(N)
print(int(sum/5))
print(N[2])

