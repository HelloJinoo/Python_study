import sys

nm_matrix = []
mk_matrix = []
result = []
NM = input().split(" ")

rowlen = int(NM[0])
for i in range(0,int(NM[0])) :
    result.append([])
    row = input().split(" ")
    for j in range(0, len(row)) :
        if j == 0 :
            nm_matrix.append([int(row[j])])
        else :
            nm_matrix[i].append(int(row[j]))

MK = input().split(" ")
collen = int(MK[1])
calnum = int(MK[0])
for i in range(0,int(MK[0])) :
    row = input().split(" ")
    for j in range(0, len(row)) :
        if j == 0 :
            mk_matrix.append([int(row[j])])
        else :
            mk_matrix[i].append(int(row[j]))

for row in range(0 , rowlen) :             # row
    for col in range(0 , collen ):         # col
        sum = 0
        for mul in range(0 , calnum) :     # 원소개수
            sum += nm_matrix[row][mul] * mk_matrix[mul][col]

        result[row].append(sum)

for i in range(0 , len(result)) :
    for j in range(0 , len(result[i])) :
        sys.stdout.write(str(result[i][j])+" ")
    print()

