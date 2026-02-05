"""
1523. Count Odd Numbers in an Interval Range
Easy
Topics
premium lock icon
Companies
Hint
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:


        # input: low(int), high(int)

        # output: output (int)
        output = 0

        #process:
    
        ## Idea 1: brute force
        # go from low to high to check the number that is not divided by 2 then add them up 
        """
        for num in range(low, high + 1):
            if num % 2 != 0:
                output += 1


        return output 
        """ 
        
        ## Idea 2: 
        ## kinda take hint
        """    
        (high - low + 1)  -> even -> number of odd and even is the same so take the result / 2

        (high - low + 1) -> odd -> then depend on high number 

        high number -> odd -> round up 
        high number -> even -> round down 
        
        """
        

        # round -> round down

        delta = high - low + 1
        if delta % 2 == 0:
            output = delta / 2
        else:
            if high % 2 == 0:
                output = round((delta - 1)/ 2)
           
            else: 
                output = round((delta + 1)/ 2)

        return output
    
    low = 8
    high = 10
    print(countOdds(0, low, high));