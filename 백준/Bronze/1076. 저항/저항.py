import sys
input = sys.stdin.readline

dic1 = {
        'black' :0,
        'brown' :1,
        'red'   :2,
        'orange':3,
        'yellow':4,
        'green' :5,
        'blue'  :6,
        'violet':7,
        'grey'  :8,
        'white' :9
        }
result = 0 
temp = []
for i in range(3):
    color = input().rstrip()
    if i == 2:
        result = int(''.join(map(str,temp))) * ( 10 ** dic1[color] )
        break
    temp.append(dic1[color])
    # print(sum)
print(result)