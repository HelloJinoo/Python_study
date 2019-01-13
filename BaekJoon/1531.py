pager = [ [ 0 for i in range(0,101)] for j in range(0, 101)]
n , m = map(int,input().split())
count = 0
'''입력받은 좌표들로 배열 모자이크종이로 채우기'''
for i in range(0,n) :
    l_x,l_y ,r_x,r_y = map(int,input().split())
    for i in range(l_x, r_x+1) :
        for j in range(l_y, r_y + 1) :
            pager[i][j] += 1

'''m보다 큰 부분 count'''
for i in range(1, 101):
    for j in range(1, 101):
       if m < pager[i][j] :
              count += 1
print(count)