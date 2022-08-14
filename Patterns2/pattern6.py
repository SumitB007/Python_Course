#*
# * *
#   * * *
#     * * * *
#   * * *
# * *
#*

row=int(input())





#*0000*0000*
#0*000*000*0
#00*00*00*00
#000*0*0*000
#0000***0000


n=int(input())
i=1
z=n
while i <=n:
    star=1
    while star<=i:   
     if(star==i):
        print("*",end='')
        print("0"*(n-i), end="")
     else:
        print("0",end='')
     star=star+1
    print("*", end = "")
    zero=1
    while zero<=n:
        if(zero-z==0):
            print("*",end='')
            z=z-1
        else:
            print("0",end='')
        zero=zero+1
        
        
    print()
    i=i+1
	
    