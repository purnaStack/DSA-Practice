"""
Pattern 8
----------

Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*********
 *******
  *****
   ***
    *

Examples:
Input: n = 4
Output:
*******
 *****
  ***
   *

Input: n = 2
Output:
***
 *

Constraints:
1 <= n <= 100

Approach:
Iterate from 0 to N-1 using a loop, where N is the number of rows. 
This loop will ensure to print each row of the pattern.
Now, run another loop from 0 to the current value of the outer loop variable. 
It will print the spaces before the asterisks as required in every row.
Then, run another loop to print the asterisks in one line — the count of asterisks 
decreases in each row using the formula: 2*N - (2*i + 1).
Move to a new line after printing each row to maintain the inverted pyramid shape of the pattern.

Complexity Analysis:
Time Complexity : O(N^2)
    The outer loop runs N times.
    The first inner loop runs (0 + 1 + 2 + ... + N-1) times.
    The second inner loop runs in decreasing order ((2*N -1) + (2*N - 3) + ... + 1).
    Hence, total operations are proportional to N^2.

Space Complexity : O(1)
    No extra space is being used to print the pattern.
"""

class Solution:
    
    # Function to print Pattern 8
    def pattern8(self, n):
        
        # Outer loop will run for rows
        for i in range(0, n):
            
            # This loop will print spaces
            for j in range(0, i):
                print(" ", end="")
            
            # This loop will print asterisks
            for j in range(0, 2 * n - (2 * i + 1)):
                print("*", end="")
                
            # Move to the next line
            print()

    def main(self):
        # Example input
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        # Call the pattern function
        sol.pattern8(N)


# Standard boilerplate to execute the main method
if __name__ == "__main__":
    Solution().main()
