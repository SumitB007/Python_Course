import math

class Fraction:
    
    #create your class here.
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
	
    def multiply(self,c):
        num=self.num * c.num
        denom=self.denom * c.denom
        self.num=num
        self.denom=denom
    
    def add(self,f):
        num=(self.num * f.denom)+(self.denom * f.num)
        denom=(self.denom* f.denom) 
        self.num=num
        self.denom=denom

    def simplify(self):
        a=math.gcd(self.num,self.denom)
        num=self.num//a
        denom=self.denom//a
        self.num=num
        self.denom=denom


    def print(self):
        print(str((self.num))+"/"+(str(self.denom)))
		
		
		    
n1,d1=map(int,input().split())
f1=Fraction(n1,d1)
t=int(input())

while(t>0):
 choice,n2,d2=map(int,input().split())

 
 f2=Fraction(n2,d2)

 if(choice==1):
    f1.add(f2)
    f1.simplify()
    f1.print()
 elif(choice==2):
    f1.multiply(f2)
    f1.simplify()
    f1.print()
 else:
    pass
	
	
    
#Driver's code goes here.
    

    
    
    
    
    
    
    
    
    
    
