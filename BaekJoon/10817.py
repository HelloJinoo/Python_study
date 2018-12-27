'''세 수중 두번째로 큰 수 '''
x = input().split(" ")

def search_max( x ,y ,z):

  if x < y :
      if y < z :
          return y
      else :
           if x < z :
               return z
           else :
                return x
  elif y < z :
      if z < x :
          return z
      else :
          if x < y :
              return y
          else :
              return x
  elif  y < x :
      if x < z :
          return x
      else :
          if y < z :
              return z
          else :
              return y
  else :
      return x

print(search_max(int(x[0]), int(x[1]) , int(x[2])))



