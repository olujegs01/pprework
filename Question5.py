def is_consecutive(a_list):
    return all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))

# Example usage:
print(is_consecutive([2, 3, 4, 5, 6, 7]))  # Output should be True
print(is_consecutive([1, 2, 4, 5]))  # Output should be False
