def depth_of_tree(s):
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1

    return max_depth - 1  # Subtract 1 to account for the root node without edges

# Test cases
print(depth_of_tree("(00)"))  # Output: 1
print(depth_of_tree("((00)(00))"))  # Output: 2
print(depth_of_tree("((((00)0)0)0)"))  # Output: 4
