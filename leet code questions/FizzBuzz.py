"""
QUESTION:  FIZZbUZZ

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
"""

#SOLUTION:

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):        # first checking if number is divisible by 3 and 5 , if so appending "FizzBuzz"
                ans.append("FizzBuzz")
            elif(i%3==0):				  # checking if number is divisible by 3 , if so appending "Fizz"
                ans.append("Fizz")
            elif(i%5==0):				  # checking if number is divisible by 5, if so append "Buzz"
                ans.append("Buzz")
            else:						  # if not divisibe by 3 and 5 appending number into the list
                ans.append(str(i))
        return ans                        # finally returning the ans
	
	
	
	
