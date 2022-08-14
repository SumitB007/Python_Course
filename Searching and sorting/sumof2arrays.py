from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    #Your code goes here
    carry = 0
    sum = 0
    i = n - 1
    j = m - 1
 
    while i >= 0 or j >= 0:
        sum = 0
        # If we have some elements left in the first array, then add it to the sum.
        if i >= 0:
            sum += arr1[i]
            i -= 1

        # If we have some elements left in the second array, then add it to the sum.
        if j >= 0:
            sum += arr2[j]
            j -= 1

        sum += carry
        lastDigit = sum % 10
        carry = sum // 10
        output.append(lastDigit)

    # If still some carry is left, then push it to the answer.
    if carry:
        output.append(carry)

    output = reversed(output)
    return output






#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1