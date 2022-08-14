# You are given a single non-negative integer, N.
# You need to print all numbers that:
#(i) occur in the range 0 to N (both inclusive)
#(ii) are a part of the fibonacci sequence
n=int(input("Enter the range : "))
a=0
b=1
c=0
for i in range(0,n+1):
   if(a<=n):
     print(a) 
     c=a+b
     a=b
     b=c
     

    
