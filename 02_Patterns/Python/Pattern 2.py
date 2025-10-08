''' Pattern 2 — Right-Angled Triangle Star Pattern

Problem Code: 99  Difficulty: Easy

📝 Problem Statement

Given an integer n, print a right-angled triangle pattern made of asterisks (*).
The first row should contain 1 star, the second row 2 stars, and so on up to n rows.

📥 Input

An integer n

📤 Output

Print a right-angled triangle pattern with n rows.

🧮 Example 1

Input:

n = 5


Output:

*
**
***
****
*****

🧮 Example 2

Input:

n = 2


Output:

*
**

⚙️ Constraints
1 ≤ n ≤ 100

💡 Approach

The outer loop runs n times for each row.

The inner loop runs from 0 to i (inclusive) to print increasing stars in each row.

Use print("*", end="") to print on the same line and print() to move to the next line.

💻 Python Solution '''
class Solution:
    # Function to print Pattern 2
    def pattern2(self, n):
        # Outer loop for rows
        for i in range(n):
            # Inner loop for columns
            for j in range(i + 1):
                print("*", end="")
            # Move to the next line after each row
            print()

if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    sol = Solution()
    sol.pattern2(n)