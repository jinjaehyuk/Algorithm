N = int(input())    
s, g, p, d = map(int,input().split())   
MVP = list(input())


sum = 0
temp = 0
for i in range(N):
    if MVP[i] == 'B':
        sum += s - 1 - temp
        temp = s - 1 - temp
    elif MVP[i] == 'S':
        sum += g - 1 - temp
        temp = g - 1 - temp
    elif MVP[i] == 'G':
        sum += p - 1 - temp
        temp = p - 1 - temp
    elif MVP[i] == 'P':
        sum += d - 1 - temp
        temp = d - 1 - temp
    elif MVP[i] == 'D':
        sum += d
        temp = d
print(sum)