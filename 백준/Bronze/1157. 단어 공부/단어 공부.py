words = input().lower()
word_list = list(set(words))

count = []
for i in word_list:
    cnt = words.count(i)
    count.append(cnt)

if count.count(max(count)) >1:
    print("?")
else:
    print(word_list[count.index(max(count))].upper())