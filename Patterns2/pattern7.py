#123456
#  23456
#    3456
#      456
#        56
#          6
#        56
#      456
#    3456
#  23456
#123456

n=int(input())
for i in range(1,n+1):
    spaces=i-1
    for j in range(i,n+1):
      print(" "*spaces,end='') 
      print(j,end='')
      spaces=0 
    print()    
    
for i in range (2,n+1):
    spaces=n-i
    a=n-i+1
    for j in range(1,i+1):
        print(" "*spaces,end='')
        print(a,end='')
        spaces=0
        a=a+1
    print()    
        