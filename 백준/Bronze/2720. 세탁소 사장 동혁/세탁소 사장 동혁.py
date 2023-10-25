T = int(input())



for i in range(T):
    q = 0
    d = 0
    n = 0
    p = 0
    C = int(input())
    q += int(C // 25)
    C %= 25
    d += int(C // 10)
    C %= 10
    n += int(C // 5)
    C %= 5
    p += int(C // 1)
    C %= 1
    print(q, d, n, p)