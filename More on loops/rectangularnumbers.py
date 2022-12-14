## Read input as specified in the question.
## Print output as specified in the question.
# Python3 Program to print rectangular
# inner reducing pattern
#4444444
#4333334
#4322234
#4321234
#4322234
#4333334  
#4444444
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
	prints(a, size);

# Driver code

# Input
n = int(input())

# function calling
innerPattern(n)


