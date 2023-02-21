N = int(input())

words =[]
for _ in range(N):
    words.append(input())    

words_list = set(words)
words_list = sorted(sorted(words_list), key = len)
for i in words_list:
    print(i)
    