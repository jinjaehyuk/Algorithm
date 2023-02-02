N = int(input())

for _ in range(N):
    M = list(input())
    sum = 0
    cnt = 0
    for i in range(len(M)):
        if M[i] == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)