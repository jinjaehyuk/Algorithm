N, M = map(int,input().split())


if N == 0: count = 0
else:
    box = list(map(int,input().split()))
    temp = 0
    count=1
    for i in range(len(box)):
        if box[i]+temp <= M:
            temp += box[i]
        else:
            temp = box[i]
            count += 1
print(count)
