#You are given the lengths of 3 sides of a valid triangle. You need to print any one of the following outputs depending on the triangle's nature.
#Print 1, if the triangle is equilateral
#Print 0, if it's isosceles
#Print -1, if it's scalene


a=int(input("Enter the 1st side: "))
b=int(input("Enter the 2nd side: "))
c=int(input("Enter the 3rd side: "))
if(a+b>c and b+c>a and c+a>b):
    if(a==b==c):
        print("Equilateral Triangle")
    elif(a==b or b==c or c==a):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Can't form a triangle of these sides") 
                   