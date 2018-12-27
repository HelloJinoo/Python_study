store = []
x = 1
while x < 10000  :
    sum =0
    input = x
    for i in range(1,int(len(str(x)))+1):
        sum += int(input) % 10
        input = int(input) / 10
    after = sum + x
    store.append(after)  #리스트에 추가
    x = x+1

x = 1
while x < 10000 :
    if not (x in store) : #리스트안에 있는지 확인 in
        print(x)
    x = x+1



