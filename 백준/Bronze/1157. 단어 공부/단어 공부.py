import collections
words = input()
words_cnt = collections.Counter(words.lower())

big_word = []
big_num = []
for k,v in words_cnt.most_common(2):
    big_word.append(k)
    big_num.append(v)

if len(big_num) == 1:
    big_num.append('')
    
if big_num[0] == big_num[1]:
    print("?")
else:
    print(big_word[0].upper())       

        