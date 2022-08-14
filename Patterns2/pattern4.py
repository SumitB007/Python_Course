#    1
#   121
#  12321
# 1234321
#123454321
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
    p=i-1
    while p>=1:
        print(p,end='')
        p=p-1     
    print()
    i=i+1     


#     1
#    232
#   34543
#  4567654
# 567898765
n=int(input())
i=1
while i <= n:
    spaces=1
    while spaces<= n-i:
        print(' ',end='')
        spaces=spaces+1
    num=i
    z=i-1
    while num<=i+z:
        print(num,end='')
        num=num+1
    num=num-1    
    p=num-1
    while p>=i:
        print(p,end='')
        p=p-1     
    print()
    i=i+1         


#      *
#     ***
#    *****
#     ***
#      *
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