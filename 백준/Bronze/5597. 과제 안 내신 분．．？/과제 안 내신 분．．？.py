sno = [i for i in range(1,31)]

for _ in range(28):
    apply = int(input())
    sno.remove(apply)

print(min(sno))
print(max(sno))      