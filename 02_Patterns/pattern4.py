'''🔢 Pattern 4 — Repeating Number Triangle Pattern

Problem Code: 102  Difficulty: Easy

📝 Problem Statement

Given an integer n, print a right-angled triangle pattern of numbers where each row contains the same number repeated as many times as the row number.

For example, for n = 5, the pattern should look like this:

1
22
333
4444
55555

📥 Input

An integer n

📤 Output

Print a triangle pattern where the i-th row contains the number i repeated i times.

🧮 Example 1

Input:

n = 5


Output:

1
22
333
4444
55555

🧮 Example 2

Input:

n = 2


Output:

1
22

⚙️ Constraints
1 ≤ n ≤ 100

💡 Approach

The outer loop runs from 1 to n to represent rows.

The inner loop runs from 1 to i to print the current row number repeatedly.

Use print(i, end="") to print numbers on the same line, then print() to move to the next line.

🧮 Complexity Analysis

Time Complexity: O(N²)
(The number of printed elements is 1 + 2 + 3 + ... + N = N*(N+1)/2)

Space Complexity: O(1)
(No extra space is used)

💻 Python Solution'''
class Solution:
    # Function to print Pattern 4
    def pattern4(self, n):
        # Outer loop for rows
        for i in range(1, n + 1):
            # Inner loop for columns
            for j in range(1, i + 1):
                print(i, end="")
            # Move to the next line after each row
            print()

if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    sol = Solution()
    sol.pattern4(n)