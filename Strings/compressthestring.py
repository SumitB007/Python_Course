#If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

#The string is compressed only when the repeated character count is more than 1.
from sys import stdin

def getCompressedString(s) :
	# Write your code here.
	n = len(s)

	# Declare empty string.
	answer = ""
	
	# Initialize current count of any character in string.
	currentCharCount = 1

	# Add first letter of string to answer.
	answer += s[0]
	
	for i in range(1, n):

		# If the current letter is same as previous.
		if s[i] == s[i - 1]:
			currentCharCount += 1
			
		else:
			if currentCharCount > 1:

				# Add count of letter in answer.
				answer += str(currentCharCount)
				currentCharCount = 1
				
			answer += s[i]

	if currentCharCount > 1:
		answer += str(currentCharCount)

	# Return answer.
	return answer

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)