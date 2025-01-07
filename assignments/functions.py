#max no three number
def max_of_three(a, b, c):
    return max(a, b, c)

#Sum of Numbers in a List
def sum_of_list(numbers):
    return sum(numbers)

print(sum_of_list([8, 2, 3, 0, 7]))  

#Multiply All Numbers in a List
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example
print(multiply_list([8, 2, 3, -1, 7]))  

#reverse string
def reverse_string(s):
    return s[::-1]

# Example
print(reverse_string("1234abcd"))  

# Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example
print(factorial(5))  # Output: 120

#6. Check if a Number is Within a Range

def in_range(num, start, end):
    return start <= num <= end

# Example
print(in_range(5, 1, 10))  # Output: True




# Count Upper and Lower Case Letters
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

# Example
upper, lower = count_case('The quick Brow Fox')
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case Characters : {lower}")
# Output: Upper: 3, Lower: 12




#Unique Elements in a List
def unique_elements(lst):
    return list(set(lst))

# Example
print(unique_elements([1, 2, 3, 3, 3, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(29))  # Output: True


#Check if a Number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(29))  # Output: True


#Even Numbers from a List
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Example
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [2, 4, 6, 8]



#12. Check if a String is a Palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("nurses run"))  # Output: True
