n = int(input())
heat = [ int(input()) for i in range(n) ]
if heat[1]-heat[0] == heat[2]-heat[1]: #등차수열 확인
    print(heat[-1] +heat[2]-heat[1])
else :                                 #등비수열 확인
    print(int(heat[-1]* (heat[2]//heat[1])))