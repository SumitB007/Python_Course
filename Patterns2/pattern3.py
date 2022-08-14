n=int(input())
i=1
while i <= n:
    spaces=1
    while spaces<= n-i:
        print(' ',end='')
        spaces=spaces+1
    num=1    
    while num<=i:
        print(num,end='')
        num=num+1
    print()
    i=i+1     



#  *
# ***
#*****
# ***
#  *    

n=int(input())
n1=(n+1)/2
n2=(n-1)/2
i=1
while i <= n1:
    spaces=1
    while spaces<= n1-i:
        print(' ',end='')
        spaces=spaces+1
    num=1    
    while num<=i:
        print('*',end='')
        num=num+1
    p=i-1
    while p>=1:
        print('*',end='')
        p=p-1     
    print()
    i=i+1 
    
i=n2

while i>=1:
    spaces=n2-i+1
    while spaces>=1:
        print(' ',end='')
        spaces=spaces-1
    num= 2*i-1
    while num>=1:
        print('*',end='')
        num=num-1
    print()
    i=i-1