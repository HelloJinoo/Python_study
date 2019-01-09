n , m = map(int,input().split(" "))
value = [ [ i for i in input().split() ] for j in range(0,n) ]
t = int(input())
a = [list(map(int,input().split(" "))) for i in range(0 , t) ]

for i in range(0, len(a)) :
    row_sub = [ value[row] for row in range(a[i][0]-1 , a[i][2])  ]
    col_sub = [ [ int(row_sub[k][col]) for col in range(a[i][1]-1 , a[i][3]) ] for k in range(0,len(row_sub))]
    result = 0
    for j in range(0, len(col_sub)) :
         result = result + sum(col_sub[j])
    print(result)