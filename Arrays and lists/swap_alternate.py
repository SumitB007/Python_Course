from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    if(n%2==0):
        for i in range(0,n+1,2):
          if(i<len(arr)):
           arr[i],arr[i+1]=arr[i+1],arr[i]
          elif(i==len(arr)):
              pass
    else:
        for i in range(0,n+1,2):
          if(i<(len(arr)-1)):
           arr[i],arr[i+1]=arr[i+1],arr[i]
          elif(i==(n-1)):
              pass
    return arr


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()



#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1