
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    string1=""
    if ch in string:
        for ele in string:
            if(ele==ch):
                pass
            else:
                string1=string1+ele
        return string1        
    
    else:
        return string



	

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)