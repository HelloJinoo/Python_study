
test = input().split(" ")
red = int(test[0])
brown = int(test[1])

#갈색에서 나올 수있는 곲들
for i in range(1, brown+1) :
    if brown % i == 0 :
        w = int(brown / i)
        if i*2 + (w*2)+4 == red :  #red타일 갯수 비교
            print(w+2 , i+2 )
            break


