case = int(input())

def commondivisor( x , y ) :
    while y != 0 :
        n = x % y
        x = y
        y = n
    return x

for i in range(0 , case) :
    num = input().split(" ")
    num_1 = int(num[0])
    num_2 = int(num[1])
    if num_1 > num_2 :
        common = commondivisor(num_1 , num_2)
    else :
        common = commondivisor(num_2 , num_1)
    mul1 = int(num_1 / common)
    mul2 = int(num_2 / common)

    print(mul1 * mul2 * common)