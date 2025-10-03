# Python Operators Examples

# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division
print("-" * 40)

# 2. Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to
print("-" * 40)

# 3. Logical Operators
x = True
y = False
print("Logical Operators:")
print("x and y:", x and y)   # AND
print("x or y:", x or y)     # OR
print("not x:", not x)       # NOT
print("-" * 40)

# 4. Bitwise Operators
m = 5   # 0101 in binary
n = 3   # 0011 in binary
print("Bitwise Operators:")
print("m & n:", m & n)   # AND
print("m | n:", m | n)   # OR
print("m ^ n:", m ^ n)   # XOR
print("~m:", ~m)         # NOT
print("m << 1:", m << 1) # Left Shift
print("m >> 1:", m >> 1) # Right Shift
print("-" * 40)

# 5. Assignment Operators
p = 10
print("Assignment Operators:")
p += 5
print("p += 5:", p)
p -= 3
print("p -= 3:", p)
p *= 2
print("p *= 2:", p)
p /= 4
print("p /= 4:", p)
p %= 3
print("p %= 3:", p)
p **= 2
print("p **= 2:", p)
p //= 2
print("p //= 2:", p)
print("-" * 40)

# 6. Membership Operators
list1 = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("3 in list1:", 3 in list1)         # True
print("10 not in list1:", 10 not in list1) # True
print("-" * 40)

# 7. Identity Operators
q = [1, 2, 3]
r = [1, 2, 3]
s = q
print("Identity Operators:")
print("q is s:", q is s)       # True (same object)
print("q is r:", q is r)       # False (different objects, same values)
print("q is not r:", q is not r) # True
