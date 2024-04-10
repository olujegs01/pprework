
Question 1

def hello_name(user_name):
    print("hello_" + user_name + "!")

# Example usage:
hello_name("USERNAME")

Question 2

def first_odds():
    for i in range(1, 101, 2):
        print(i)

# Example usage:
first_odds()


Question 3

def max_num_in_list(a_list):
    return max(a_list)

# Example usage:
print(max_num_in_list([1, 3, 5, 7, 9]))

Question 4

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

# Example usage:
print(is_leap_year(2024))  # Output should be True


Question 5

def is_consecutive(a_list):
    return all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))

# Example usage:
print(is_consecutive([2, 3, 4, 5, 6, 7]))  # Output should be True
print(is_consecutive([1, 2, 4, 5]))  # Output should be False

