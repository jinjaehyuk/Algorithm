K = int(input())
kl = []
for _ in range(K):
    num = int(input())
    if num == 0:
        kl.pop()
    else:
        kl.append(num)       
print(sum(kl))
