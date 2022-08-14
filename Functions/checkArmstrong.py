def checkArmstrong(num):
   count=0
   temp=num
   sum=0
   while num>0:
    num=num//10
    count+=1

   while temp>0:
    digit=temp%10
    sum= sum + ((digit)**count)
    temp=temp//10        
   if(sum==n):
    return True    
 
n=int(input())
isArmstrong= checkArmstrong(n)
if(isArmstrong):
    print("true")
else:
    print("false")
