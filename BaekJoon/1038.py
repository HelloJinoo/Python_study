N = int(input())
decrease_num = [ [0,1,2,3,4,5,6,7,8,9 ] ]
count = 0

# DP를 이용하여 감소하는 수 만들기
while count < N:
    list = []
    for first in range(1,10) :
         for second in range(0 , len(decrease_num[len(decrease_num)-1]) ) :
             st = str(decrease_num[len(decrease_num)-1][second])
             if first > int(st[0]) :
                 count += 1
                 st = str(first) + st
                 list.append(st)
    decrease_num.append(list)
    if '9876543210' in list :
        break

index = 0
row = N
total_count = 0
stop = 0

#출력 인덱스 찾기
for i in range(0 , len(decrease_num)) :
    total_count += len(decrease_num[i])
    if len(decrease_num[i]) <= row and stop == 0:
        index += 1
        row = row - len(decrease_num[i])
    else :
        stop = 1


if N >= total_count:
    print(-1)
else :
    print(decrease_num[index][row])

