n , m = map(int , input().split())
sheet = []
for i in range(0 , n):
    time = int(input())
    for j in range(0 , time) :
        sheet.append(i+1)
for i in range(0,m) :
    current = int(input())
    print(sheet[current])