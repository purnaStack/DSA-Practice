'''Pattern 1 — Square Star Pattern

Problem Code: 162  Difficulty: Easy

📝 Problem Statement

Given an integer n, print a square pattern made of asterisks (*).
Each row and column of the square should contain n stars.

📥 Input

An integer n

📤 Output

Print a square pattern of stars having n rows and n columns.

🧮 Example 1

Input:

n = 5


Output:

*****
*****
*****
*****
*****

🧮 Example 2

Input:

n = 2


Output:

**
**

⚙️ Constraints
1 ≤ n ≤ 100

- Use **two nested loops**:
  - The **outer loop** runs `n` times to print each row.
  - The **inner loop** runs `n` times to print `n` asterisks in a row.
- Use `print("*", end="")` to print asterisks on the same line.
- After each row, use `print()` to move to the next line.

---
'''
# ================= Python Solution =================
# Run this part with Python interpreter (python filename.py)
class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    sol = Solution()
    sol.pattern1(n)

# ================= Java Solution =================
''' Run this part with Java compiler (javac filename.java)
   and then java filename

class Solution {
    // Function to print pattern1
    public void pattern1(int n) {
        
        // Outer loop will run for rows.
        for (int i = 0; i < n; i++) {
            
            // Inner loop will run for columns.
            for (int j = 0; j < n; j++) {
                System.out.print("*");
            }
            /* As soon as n stars are printed, move
            to the next row and give a line break. */
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int N = 4;

        // Create an instance of the Solution class
        Solution sol = new Solution();

        sol.pattern1(N);
    }
}
'''