def isleap(n):
    if (((n%4==0)and(n%100!=0))or(n%400==0)):
       return 1
    return 0

n=int(input())
l=[]
t=0
if(isleap(n)):
    n+=4
else:
    n+=4-(n%4)
for i in range(15):
    y=n+i*4
    if(isleap(y)):
        l.append(y)
    else:
        t+=1
if(t==1):
    l.append(n+15*4)

    
        
