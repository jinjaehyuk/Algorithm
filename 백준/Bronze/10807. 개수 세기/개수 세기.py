
N = int(input())
if (N >=1 and N<= 101):
    N_list = list(map(int, input().split()))
    v = int(input())
    if v >= -100 and v <= 100:
      print(N_list.count(v))