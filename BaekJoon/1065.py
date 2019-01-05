N = int(input())
count = 0
if N < 100 :
    count = N
else :
    count = 99

for i in range(100 , N+1) :
     st = str(i)
     d = int(st[0]) - int(st[1])
     comp =0
     for j in range(1, len(str(i))-1) :
        if int(st[j]) - int(st[j+1]) != d :
                comp = 1
                break
     if comp == 0 :
          count += 1


print(count)

