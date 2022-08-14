
from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
    string1=string[0]
    for i in range(0,len(string)-1):
        a=string[i]
        for j in range(i+1,len(string)):
            if(string[j]==a):
                break
            else:
                string1=string1+string[j]
                break

    string=string1
    return string








#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)