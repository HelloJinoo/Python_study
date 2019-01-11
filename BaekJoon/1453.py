n = int(input())
seat = [0]*101
count = 0
want = list(map(int,input().split()))
for i in want:
    if seat[i] == 0 :    # 자리부여
        seat[i] = 1;
    else :               # 원하는 자리에 사람이 있음
      count += 1
print(count)