n=int(input("Enter how many numbers u want to take : "))
l=0
for i in range(0,n):
    a=int(input("Enter the no: "))
    if(a>=l):
        l=a
    else:
        l=l+0
print(l," is the largest number")
