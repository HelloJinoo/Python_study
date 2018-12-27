case = input()

for i in range(0,int(case)) :
    info = input().split(" ")
    people = int(info[0])
    sum  =0
    for jumsu in range( 1 , int(people)+1) :
           sum += int(info[jumsu])

    ave = float(sum) / people
    count =0
    for index in range(1 , int(people)+1) :
        if float(info[index]) > float(ave) :
             count = int(count) +1

    result = round(count /people * 100,3)  # 소수점 3번째 자리에서 반올림
    print("%0.3f" % result + "%")  #소수점 3자리 까지 출력하는 포맷