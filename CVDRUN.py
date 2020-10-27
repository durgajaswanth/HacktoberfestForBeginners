for i in range(int(input())):
    n,k,x,y = [int(i) for i in input().split()] 
    e=(x+k)%n
    f = 0
    while(e!=x):
          if(e==y):
              f=1
              break 
          e=(e+k)%n
    if(x==y):
              f=1 
    if f==1:      
       print('YES') 
    if f==0:      
       print("NO")   