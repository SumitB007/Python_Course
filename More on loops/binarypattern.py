#1111
#000
#11
#0

n=int(input())

for i in range (1,n+1,1):
    if(i%2==0):
        a=0
    else:
        a=1
    for j in range(0,n-i+1):
        print(a,end='')
    print()    




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
    



#4444444
#4333334
#4322234
#4321234
#4322234
#4333334  
#4444444




## Read input as specified in the question.
## Print output as specified in the question.
# Python3 Program to print rectangular
# inner reducing pattern
MAX = 100

# function to Print pattern
def prints(a, size):
	for i in range(size):
		for j in range(size):
			print(a[i][j], end = '')
		print()

# function to compute pattern
def innerPattern(n):
	
	# Pattern Size
	size = 2 * n - 1
	front = 0
	back = size - 1
	a = [[0 for i in range(MAX)]
			for i in range(MAX)]
	while (n != 0):
		for i in range(front, back + 1):
			for j in range(front, back + 1):
				if (i == front or i == back or
					j == front or j == back):
					a[i][j] = n
		front += 1
		back -= 1
		n -= 1
	prints(a, size)

# Driver code

# Input
n = int(input())

# function calling
innerPattern(n)



# 1    2   3    4   5
# 11   12  13   14  15
# 21   22  23   24  25
# 16   17  18   19  20
# 6    7    8   9   10


import math

n = int(input())

for i in range(math.ceil(n/2)):

   for j in range(1,n+1):

       print(n*2*i + j ,end = " ");

   print()

for i in range(n//2,0,-1):

   for j in range(1,n+1):

       print(n*(2*i-1) + j , end = " ")

   print()