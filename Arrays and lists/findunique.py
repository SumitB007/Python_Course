import sys

def findUnique(arr, n) :
    #Your code goes here
    for i in range(0,n):
        count=arr.count(arr[i])
        if(count==1):
            return arr[i]
    

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    c=findUnique(arr, n)
    print(c)   
    t -= 1
    
    
    