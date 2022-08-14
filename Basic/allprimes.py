# You are given a single positive integer, N. 
# You need to print all prime numbers that occur
# in the range 1 to N (both inclusive).
n=int(input("Enter a number : "))
if(n>2):
    for i in range(2,n+1):
        a=0
        for j in  range(2,i):    
            if(i%j==0):
              a=a+1
            else:
              a=a+0
        if(a==0):
          print(i)
       
elif(n==2):
    print(n)
else:
    print("Enter a number greater than 1")     
    