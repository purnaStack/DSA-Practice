"""
Pattern 5
----------

Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*****
****
***
**
*

Examples:
Input: n = 4
Output:
****
***
**
*

Input: n = 2
Output:
**
*

Constraints:
1 <= n <= 100

Approach:
Use a for loop to iterate from 0 to N-1, where N is the number of rows. 
This loop will ensure to print each row of the pattern.
Inside this loop, run another loop from 0 to (N - current value of the outer loop variable). 
It will decrease the number of columns as the row value increases.
Now, print the asterisk in the inner loop all in one line, to complete the current row.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.

Complexity Analysis:
Time Complexity : O(N^2)
Space Complexity : O(1)
"""

class Solution:
    
    # Function to print Pattern 5
    def pattern5(self, n):
        
        # Outer loop will run for rows.
        for i in range(0, n):
            
            # Inner loop will run for columns.
            for j in range(0, n - i):
                print("*", end="")
            
            # Move to the next line after printing each row
            print()

    def main(self):
        # Example input
        N = 5
        
        # Create an instance of Solution class
        sol = Solution()
        
        # Call the pattern function
        sol.pattern5(N)


# Standard boilerplate to execute the main method
if __name__ == "__main__":
    Solution().main()
