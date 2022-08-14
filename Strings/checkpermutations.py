from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    count=0
    a=0
    b=0
    if (len(string1)==len(string2)):
        for ele in string1:
           if(ele not in string2):
               return False  
           elif(ele in string2): 
            a=string1.count(ele)
            b=string2.count(ele)
           else:
               return False 
            

           if(a==b):
            count=count+1
           else:
            count=0   
        if(count>0):
            return True
        else:
            return False    
    
    else:
        return False        
            
                    

 



#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

