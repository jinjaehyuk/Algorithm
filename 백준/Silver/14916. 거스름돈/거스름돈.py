money = int(input())    
count = 0
while True:
    if money % 5 == 0:
        count += int(money // 5)
        break
    else:
        money -= 2
        count+= 1
    
    if money < 0:
        break
if money < 0:
    print(-1)
else:
    print(count)
        
    