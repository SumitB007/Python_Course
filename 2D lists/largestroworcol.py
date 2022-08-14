'''

For a given two-dimensional integer array/list of size (N x M), 
you need to find out which row or column has the
largest sum(sum of all the elements in a row/column) amongst all the rows and columns.

In order to print two or more integers in a line separated by a single 
space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(mat, nRows, mCols):
    #Your code goes here
    max_sum=-2147483648
    row_index=0
    col_index=0
    col_max=0
    row_max=0
       
    
    #column
    for j in range(mCols):
        col_sum=0   
        for ele in mat:
            col_sum=col_sum+ele[j]
        if(col_sum>col_max):
            col_max=col_sum
            col_index=j

    #row
    for i in range(nRows):
        row_sum=0
        for j in range(mCols):
            row_sum=row_sum + mat[i][j]
        if(row_sum>row_max):
            row_max=row_sum
            row_index=i   

    if(row_max>=col_max):
        if(row_max==0):
            print("row 0 -2147483648")
        else:    
            print("row ",row_index," ",row_max)
    else:
        print("column ",col_index," ",col_max)
     


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)
    t -= 1