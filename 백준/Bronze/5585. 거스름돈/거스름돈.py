N = int(input())
l = 1000 - N
cnt = 0

arrM = [500, 100, 50, 10, 5, 1]

for i in range(len(arrM)):
    cnt += int(l/arrM[i])
    l %= arrM[i]
print(cnt)