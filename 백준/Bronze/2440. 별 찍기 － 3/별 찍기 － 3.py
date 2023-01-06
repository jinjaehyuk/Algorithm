N = int(input())

for i in reversed(range(N)):
    for j in range(i+1):
        print('*',end='')
    print()