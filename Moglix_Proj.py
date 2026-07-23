def longest_valid_parentheses(s: str) -> int:
    max_len = 0
    stack = [-1]  
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()
            if not stack:
                stack.append(i)  
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


# Test cases
print(longest_valid_parentheses("(()"))   # Output: 2
print(longest_valid_parentheses(")()())")) # Output: 4
print(longest_valid_parentheses(""))      # Output: 0
