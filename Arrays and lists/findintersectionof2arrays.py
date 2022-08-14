
import sys

            
def findArrayIntersection(arr1,n,arr2,m):
	ans = list()
	i,j = 0,0
	while i<n and j<m:
		if arr[i] == brr[j]:
			ans.append(arr[i])
			i+=1
			j+=1

		elif arr[i] > brr[j]:
			j+=1

		else:
			i+=1

	return ans
#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
   
#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    c=findArrayIntersection(arr1, n, arr2, m)
    printList(c,len(c))

    t -= 1