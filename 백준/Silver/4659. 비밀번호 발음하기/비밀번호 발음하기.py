import sys 
input = sys.stdin.readline

con = ['a','e','i','o','u']
while True:
    t = input().rstrip()
    if t == 'end':
        break
    
    pw =list(t)
    v_flag =0
    v_cnt = 0
    c_cnt = 0
    err = 0
    for i in range(len(pw)):
        if i > 0:
            if pw[i] == pw[i-1]:
                if pw[i] != 'e' and pw[i]!='o':
                    err = 1
                    break
        if pw[i] in con:
            v_flag = 1
            v_cnt += 1
            c_cnt=0
            if v_cnt ==3:
                err=1
                break
        else:
            v_cnt = 0
            c_cnt += 1
            if c_cnt ==3:
                err =1
                break
    if (err != 1) and (v_flag == 1):
        print("<"+ t +"> is acceptable.")
    else:
	    print("<" + t + "> is not acceptable.")