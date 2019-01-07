x ,y = input().split(" ")
x_re =""
y_re= ""
for i in range(len(x)-1 , -1, -1) :
    x_re += x[i]
    y_re += y[i]
print(max(int(x_re) , int(y_re)))