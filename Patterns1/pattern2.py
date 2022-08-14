#n=4
#1
#11
#202
#3003
num=int(input())
i=1
while i<=num:
    j=0
    while j<i:
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0:
                print(x,end="")
            else:print(0,end="")
        j=j+1    
    i=i+1        
    print("")
#n
#1
#11
#121
#1221
num=int(input())
i=1
while i<=num:
    j=0
    while j<i:
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0:
                print(1,end="")
            else:print(2,end="")
        j=j+1    
    i=i+1        
    print("")