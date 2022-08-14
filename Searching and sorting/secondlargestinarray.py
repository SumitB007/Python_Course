# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin
import sys


def secondLargestElement(arr, n):
    #Your code goes here)
    largest = -sys.maxsize + 1
    secondLargest = -sys.maxsize + 1

    # Find largest and second largest element simultaneously.
    for i in range(0, n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]

        # If an element is smaller than largest and smaller than second largest.
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]

    if(secondLargest == -sys.maxsize+1):
        return -(2**31)

    return secondLargest





#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1