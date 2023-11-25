import sys 
input = sys.stdin.readline

subject = [0]* 1001
n = int(input())
w = []

for _ in range(n):
    w.append(list(map(int,input().split())))
w = sorted(w, key=lambda x:x[1], reverse=True)
i = 0
while True:
    d = w[i][0]
    score = w[i][1]
    if subject[d] == 0:
        subject[d] = score
    else:
        for j in range(d,0,-1):
            if subject[j] == 0:
                subject[j] = score
                break
            elif j == 0 and subject[j] != 0:
                break

    if i == n-1:
        break
    i += 1
print(sum(subject))