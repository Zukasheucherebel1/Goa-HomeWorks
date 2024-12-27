def valid_braces(string):
    stack = []
    matching_braces = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching_braces[char]:
                return False
            stack.pop()
    
    return not stack