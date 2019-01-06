import sys
case = int(input())
people = []

class Human_info :
    def __init__(self , weight , height):
        self.weight = weight
        self.height = height

for i in range(0, case) :
    info = input().split(" ")
    people.append(Human_info(int(info[0]) , int(info[1])))  #사람의 키와 몸무게 정보 저장

for standard in range(0 , len(people)) :
    count = 0 # 등치가 큰 사람 수
    for comp in range(0 , len(people)) :
        if standard == comp :
            continue
        else :
           if people[standard].weight < people[comp].weight :      #덩치 비교
               if people[standard].height < people[comp].height :
                   count += 1

    sys.stdout.write(str(count+1) + " ")