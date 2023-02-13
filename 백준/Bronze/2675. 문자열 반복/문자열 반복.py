T = int(input())

for i in range(T):
    R,S = input().split()
    words=''
    for j in range(len(S)):
        for k in range(int(R)):
            words += S[j]
    print(words)