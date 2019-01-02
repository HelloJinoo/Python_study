input_str = input().split(" ")
str = input_str[0]
str2 = input_str[1]

mincount = len(str)
if len(str) == len(str2) :
    count = 0
    for i in range(0,len(str)) :
        if str[i] != str2[i] :
            count = count + 1
    mincount = count
else :
    differ = len(str2) - len(str)
    for j in range(0, differ+1) :
        count = 0
        for i in range(0,len(str)) :
            if str[i] != str2[i+j] :
                count = count +1

        if mincount > count :
            mincount = count

print(mincount)
