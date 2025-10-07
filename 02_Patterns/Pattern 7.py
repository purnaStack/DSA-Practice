"""
Pattern 7
----------

Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

    *
   ***
  *****
 *******
*********

Examples:
Input: n = 4
Output:
   *
  ***
 *****
*******

Input: n = 2
Output:
 *
***

Constraints:
1 <= n <= 100

Approach:
Iterate from 0 to N-1, where N is the number of rows. 
This loop will ensure to print each row of the pattern.
Now, run another loop from 0 to (N - current row index - 1). 
It will print the spaces before the asterisks as required in every row.
Again, run a loop to print the asterisks (2*i + 1 in number) in one line.
Move to a new line after printing each row to maintain the pyramid shape of the pattern.

Complexity Analysis:
Time Complexity : O(N^2). 
The outer loop runs N times. 
The first inner loop runs (N-1 + N-2 + ... + 1) times, 
and the second inner loop runs incrementally in each iteration (1 + 3 + 5 + ... + 2*N - 1). 
Overall, it results in O(N^2).

Space Complexity : O(1). 
As no extra space is being used to print the patterns.
"""

class Solution:
    
    # Function to print Pattern 7
    def pattern7(self, n):
        
        # Outer loop will run for rows
        for i in range(0, n):
            
            # Loop to print spaces
            for j in range(0, (n - i - 1)):
                print(" ", end="")
            
            # Loop to print asterisks
            for j in range(0, 2 * i + 1):
                print("*", end="")

            # Move to the next line
            print()

    def main(self):
        # Example input
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        # Call the pattern function
        sol.pattern7(N)


# Standard boilerplate to execute the main method
if __name__ == "__main__":
    Solution().main()
