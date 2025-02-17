class Solution:
    def isValid(self, s: str) -> bool:  # Define a method inside the class
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop from stack or use a dummy value
                if mapping[char] != top_element:
                    return False
            else:  # If it's an opening bracket
                stack.append(char)

        return not stack  # Stack should be empty if valid

# Create an instance of the Solution class
solution = Solution()

# Test Cases
print(solution.isValid("()"))       # True
print(solution.isValid("()[]{}"))   # True
print(solution.isValid("(]"))       # False
print(solution.isValid("([])"))     # True
print(solution.isValid("{[]}"))     # True
print(solution.isValid("{[}]"))     # False
