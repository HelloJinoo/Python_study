import sys

TAERGET_NUM = 100

my_sum = 0
data = []
for _ in range(9):
    temp = int(sys.stdin.readline())
    data.append(temp)
    my_sum += temp

data = sorted(data)

# 2개를 빼서 비교
for i in range(9):
    for j in range(9):
        temp = data[i] + data[j]
        if my_sum - temp == TAERGET_NUM:
            for k in range(9):
                if k != i and k != j:
                    print(data[k])
            sys.exit()



