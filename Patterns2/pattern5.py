#1        1
#12      21
#123    321
#1234  4321
#1234554321

n=int(input())
i=1
n1=n
n2=2*n


while i<=n1:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    while j<=n2:
        if((n2-j)<=i):
            if((n2-j+1)>i):
                print(" ",end='')
            else:
             print(n2-j+1,end='')
        else:
         print(" ",end='')
        j=j+1
    print()                                   
    i=i+1



#   1
#  212
# 32123
#4321234
row=int(input())
i=1
while i<=row:
    j=1
    while j<=(row-i):
        print(" ",end='')
        j=j+1
    j=i
    while j>=1:
        print(j,end='')
        j=j-1
    j=2
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i+1 


#OR
n=int(input())
for i in range (1,n+1,1):
    for s in range(n-i):
        print(" ",end='')
    for j in range (i, 2*i,1):
        print(j,end='')
    for j in range (2*i-2,i-1,-1):
        print(j,end='')
    print()                



