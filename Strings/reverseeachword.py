
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
    stri=""
    li=string.split()
    for ele in li:
      a=len(ele)
      ele=ele[a::-1]+" "
      stri=stri+ele
    return stri 



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)