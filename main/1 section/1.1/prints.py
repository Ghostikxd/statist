def prints(txt,x,f):
    kr=len(x)
    print(txt,file=f)
    for i in range(kr):
         if(i<(kr-1)):print(x[i],end=" ",file=f)
         if(i==(kr-1)):print(x[i],file=f)