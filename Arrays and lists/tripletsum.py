
from sys import stdin

def findTriplet(arr, n, x) :
    #Your code goes here
    count=0
    for i in range(0,n-2):
        a=arr[i]
        for j in range(i+1,n-1):
            b=arr[j]
            for k in range(j+1,n):
                c=arr[k]
                if(a+b+c==x):
                    count=count+1
                else:
                    pass
                
    #return your answer
    return count

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1