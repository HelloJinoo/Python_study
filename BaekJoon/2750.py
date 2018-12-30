case = input()
l = []

for i in range(0 , int(case)) :
    x = int(input())
    if len(l) == 0 :
        l.append(x)
    else :
        change = -1
        for index in range(0, len(l)) :
            if l[index] > x :
                change = index
                break
        if change == -1 :
            l.append(x)
        else :
            l.insert(change , x)

for i in range(0 , len(l)) :
    print(l[i])
