n=int(input("Enter a number : "))
a=0
if(n>2):
    for i in range(2,n):
        if(n%i==0):
            a=a+1
        else:
            a=a+0
    if(a>=1):
      print(n," is not a prime number")
    elif(a==0):
      print(n," is a prime number") 
elif(n==2 or n==1):
    print(n ," is a prime number")
else:
    print("Enter a number greater than 0")
