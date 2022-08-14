#You are given two numbers. You need to calculate 
#and print their greatest common divisor (GCD).
a=int(input("Enter the 1st no. : "))
b=int(input("Enter the 2nd no. : "))
gcd=1
if(a==b):
    print("GCD is ",a)
else:
   if(a>b):
       a=a
       b=b
   else:
       temp=a
       a=b
       b=temp

   for i in range(1,a+1):
       if(a%i==0 and b%i==0):
           gcd=i
print("GCD is ",gcd)

