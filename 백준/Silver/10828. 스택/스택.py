import sys
N = int(input())
stack = []
for _ in range(N):
    str = sys.stdin.readline().rstrip()
    str = str.split(' ')
    if str[0] == "push":
        stack.append(int(str[1]))
    elif str[0] == "pop":
        try:
            print(stack[len(stack)-1])
            stack.pop()
        except:
            print("-1")
    elif str[0] == "size":
        print(len(stack))
    elif str[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")
    elif str[0] == "top":
        try:
            print(stack[len(stack)-1])
        except:
            print("-1")