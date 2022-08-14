n=int(input())
n1=0
n2=0
while n>0:
    n2=n1*10
    n1=n%10
    n=n//10
    n1=n1+n2
           
print(n1)