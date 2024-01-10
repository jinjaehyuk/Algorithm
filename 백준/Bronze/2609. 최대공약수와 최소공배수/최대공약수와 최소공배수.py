import sys
input = sys.stdin.readline

a, b = map(int,input().split())

def gcd(x, y):
    if x % y == 0:
        return y

    return gcd(y, x % y)

gcd_value = gcd(a,b)
print(gcd_value)
print((int)((a * b) / gcd_value))