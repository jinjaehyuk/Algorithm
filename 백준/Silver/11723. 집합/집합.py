import sys 
input = sys.stdin.readline

m = int(input())  
s = []  
for _ in range(m):
    cmds = input().rstrip().split()
    cmd =cmds[0]
    if cmd !="all" and cmd !="empty":
        num = int(cmds[1])
    if cmd =="add":
        if not num in s:
            s.append(num)
    elif cmd == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif cmd == "remove":
        if num in s:
            s.remove(num)
    elif cmd == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.append(num)
    elif cmd == "all":
        s = [i for i in range(1,21)]
    elif cmd == "empty":
        s = []
        
        