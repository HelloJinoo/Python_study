fibo = [0,1]
n = input()
def fibonacci(x) :
   for i in range(0 , int(x)-1) :
       fibo.append(fibo[i] + fibo[i+1])
   return fibo[len(fibo)-1]

print(fibonacci(n))

