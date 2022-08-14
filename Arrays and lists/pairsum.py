
from sys import stdin


def pairSum(arr, n, x) :
    #Your code goes here
    count=0
    for i in range(0,n-1):
        a=arr[i]
        for j in range(i+1,n):
            b=arr[j]
            if(a+b==x):
                count=count+1
            else:
                pass
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
    c=print(pairSum(arr, n, x))

    t -= 1