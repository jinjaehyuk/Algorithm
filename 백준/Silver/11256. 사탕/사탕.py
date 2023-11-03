T = int(input())    


for i in range(T):
    j, N = map(int,input().split())
    data = []
    for i in range(N):
        R, C = map(int,input().split())
        data.append(R*C)
    result = 0    
    data.sort(reverse=True)
    
    for i in range(len(data)):
        j -= data[i]
        result += 1
        if j <= 0 :
            print(result)
            break

         
