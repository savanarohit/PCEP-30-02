# Type Casting - Type casting in Python refers to the process of changing the data type of a variable from one type to another. It allows you to convert a value from one type to a compatible type.

# Integer to String
num = 10
num_str = str(num)
print(num_str)  # Output: "10"
print(type(num_str))  # Output: <class 'str'>

# String to Integer
num_str = "20"
num = int(num_str)
print(num)  # Output: 20
print(type(num))  # Output: <class 'int'>

# String to Float
float_str = "3.14"
num = float(float_str)
print(num)  # Output: 3.14
print(type(num))  # Output: <class 'float'>


# Bit Operators - Bitwise operators in Python are used to perform operations at the bit level of binary representations of integers. They manipulate individual bits of an integer or boolean values.

# Bitwise AND (&)
a = 5  # binary: 0101
b = 3  # binary: 0011

result = a & b  # binary: 0001 (decimal: 1)
print(result)  # Output: 1

# Bitwise OR (|):
a = 5  # binary: 0101
b = 3  # binary: 0011

result = a | b  # binary: 0111 (decimal: 7)
print(result)  # Output: 7

# Bitwise XOR (^)
a = 5  # binary: 0101
b = 3  # binary: 0011

result = a ^ b  # binary: 0110 (decimal: 6)
print(result)  # Output: 6

# Bitwise NOT (~):
a = 5  # binary: 0101

result = ~a  # binary: 1010 (decimal: -6)
print(result)  # Output: -6

# Bitwise left shift (<<)
a = 5  # binary: 0101

result = a << 2  # binary: 010100 (decimal: 20)
print(result)  # Output: 20

# Bitwise right shift (>>)
a = 5  # binary: 0101

result = a >> 2  # binary: 0001 (decimal: 1)
print(result)  # Output: 1
