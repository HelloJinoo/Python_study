number = int(input())
result = 0
for num in range(number , 0 , -1) :
         if num + sum([int(j) for j in str(num)]) == number:
             result = num

print(result)


