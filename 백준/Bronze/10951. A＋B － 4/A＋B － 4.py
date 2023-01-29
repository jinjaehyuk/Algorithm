##종료문구없어 예외처리
while True:   
    try:
      A, B = map(int, input().split())
      print(A+B)
    except:
        break

        