station = []

for i in range(0,4) :
    info = input().split(" ")
    station.append([int(info[0]),int(info[1])])

maxnum = int(station[0][1])
people = int(station[0][1])

for i in range(1 ,4) :
    people = people - station[i][0]
    people = people + station[i][1]
    if maxnum < people :
        maxnum = people

print(maxnum)
