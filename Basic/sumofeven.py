# You are given a single positive integer, N.
# You need to calculate and print the sum of all even numbers 
# till N(inclusive)
n=int(input("Enter a number : "))
sum=0
#for i in range (0,n+1,2):
    #print(i)
for i in range (0,n+1):
    if(i%2==0):
        sum=sum+i
    else:
        continue 
print(sum)         



             