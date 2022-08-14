#You are given a single non-negative integer, N. 
#You need to find out whether N is a part of the fibonacci sequence.
#Print "Yes" if it is and "No" if it's not.

n=int(input("Enter the range : "))
a=0
b=1
c=0
for i in range(0,n+1):
    if(a<n):
     c=a+b
     a=b
     b=c
if(a==n):
  print("Yes")
else:
  print("No")       
    






def checkMember(n):
#Implement Your Code Here
    a=0
    b=1
    c=0
    for i in range(0,n+1):
        if(a<n):
            c=a+b
            a=b
            b=c
    if(a==n):
        return True
    

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")