"""
Pattern 9
----------

Given an integer n. You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

Examples:
Input: n = 4
Output:
   *
  ***
 *****
*******
*******
 *****
  ***
   *

Input: n = 2
Output:
 *
***
***
 *

Constraints:
1 <= n <= 100

Approach:
This pattern is a combination of a pyramid and an inverted pyramid. 
First, print the pyramid and then print the inverted one.

For the upper (pyramid) part:
- Use nested loops — first loop prints spaces, second prints asterisks.
- The number of spaces decreases, while the number of asterisks increases in each row.

For the lower (inverted pyramid) part:
- Use nested loops again — first loop prints spaces, second prints asterisks.
- The number of spaces increases, while the number of asterisks decreases in each row.

After each inner loop set, move to a new line to print the next row.

Complexity Analysis:
Time Complexity: O(2 * N^2)
    Both the pyramid and inverted pyramid take O(N^2) each.
Space Complexity: O(1)
    No extra space is being used.
"""

class Solution:

    def pattern9(self, n):
        """Prints the complete diamond pattern."""
        self.erect_pyramid(n)
        self.inverted_pyramid(n)

    def erect_pyramid(self, n):
        """Prints the upper pyramid."""
        for i in range(n):
            # Print spaces
            for j in range(n - i - 1):
                print(" ", end="")

            # Print stars
            for j in range(2 * i + 1):
                print("*", end="")

            # Move to next line
            print()

    def inverted_pyramid(self, n):
        """Prints the lower inverted pyramid."""
        for i in range(n):
            # Print spaces
            for j in range(i):
                print(" ", end="")

            # Print stars
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")

            # Move to next line
            print()


# Standard boilerplate to run the code
if __name__ == "__main__":
    N = 5

    # Create instance of Solution class
    sol = Solution()

    # Call the pattern9 function
    sol.pattern9(N)
