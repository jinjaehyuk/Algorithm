N = int(input())
i = 1
sum = 0
while True:
    sum += i
    if sum > N:
        i -= 1
        break

    i += 1
print(i)