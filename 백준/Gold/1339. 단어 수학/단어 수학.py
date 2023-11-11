N = int(input())

a = []
for _ in range(N):
    a.append(input())

b = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
for words in a:
    for i in range(len(words)):
        x = len(words)-1 -i
        if words[i] in b:
            b[words[i]] += 10 ** x

words_sort = sorted(b.values(), reverse=True) 
result = 0 
num = 9 
for k in words_sort:
    if k == 0:
        break
    result += k * num
    num -= 1
print(result)