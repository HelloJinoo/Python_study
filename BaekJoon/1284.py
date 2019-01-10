x = int(input())
value = [ 4,2,3,3,3,3,3,3,3,3]
while x != 0 :
    result = 0
    str_x = str(x)
    for i in range(0,len(str_x)) :
        result += value[int(str_x[i])]
    result += len(str_x)+1
    print(result)
    x = int(input())