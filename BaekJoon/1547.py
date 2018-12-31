table = [-1, 1 ,2 , 3]

suffle = int(input())
def search_index(x) :
    index = 0
    for i in range(1, len(table)) :
        if int(x) == table[i] :
            index = i
            break
    return index

for i in range(0, suffle) :
    change = input().split(" ")
    cup_change1 = int(change[0])
    cup_change2 = int(change[1])

    index = search_index(cup_change1)
    index2 = search_index(cup_change2)
    table[index] = cup_change2
    table[index2] = cup_change1

print(table[1])