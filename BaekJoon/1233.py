s1 , s2 ,s3 =  map(int , input().split())
value = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1 ,s1+1 ) :
    for j in range(1 , s2 +1) :
        for k in range(1 , s3+1) :
            value[i+j+k] += 1
max_value = 0
result = 0
for i in range(1,len(value)) :
    if max_value < value[i] :
        max_value = value[i]
        result = i
print(result)