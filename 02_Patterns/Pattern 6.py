"""
Pattern 6
----------

Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

12345
1234
123
12
1

Examples:
Input: n = 4
Output:
1234
123
12
1

Input: n = 2
Output:
12
1

Constraints:
1 <= n <= 100

Approach:
Use a for loop to iterate from 0 to N-1, where N is the number of rows. 
This loop will ensure to print each row of the pattern.
Inside this loop, run another loop from 0 to (N - current value of the outer loop variable). 
It will ensure to decrease the number of columns as the row value increases.
Now, print the current value of inner loop + 1, which prints column numbers starting from 1 to N.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.

Complexity Analysis:
Time Complexity : O(N^2)
Space Complexity : O(1)
"""

class Solution:
    
    # Function to print Pattern 6
    def pattern6(self, n):
        
        # Outer loop will run for rows
        for i in range(0, n):
            
            # Inner loop will run for columns
            for j in range(0, n - i):
                print(j + 1, end="")
            
            # Move to next line after printing each row
            print()

    def main(self):
        # Example input
        N = 5
        
        # Create an instance of Solution class
        sol = Solution()
        
        # Call the pattern function
        sol.pattern6(N)


# Standard boilerplate to execute the main method
if __name__ == "__main__":
    Solution().main()
