S = list(input())
li = [-1 for _ in range(26)]

for i in range(len(S)):
    li[ord(S[i])-97] = S.index(S[i])

for i in range(26):
    print(li[i],end =' ')