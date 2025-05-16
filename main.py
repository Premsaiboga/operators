# Python Operators Examples

print("=== 1. Arithmetic Operators ===")
a = 10
b = 3
print("a + b =", a + b)     # Addition
print("a - b =", a - b)     # Subtraction
print("a * b =", a * b)     # Multiplication
print("a / b =", a / b)     # Division
print("a % b =", a % b)     # Modulus
print("a ** b =", a ** b)   # Exponentiation
print("a // b =", a // b)   # Floor Division

print("\n=== 2. Assignment Operators ===")
x = 5
print("x =", x)
x += 3
print("x += 3 →", x)
x -= 2
print("x -= 2 →", x)
x *= 4
print("x *= 4 →", x)
x /= 6
print("x /= 6 →", x)
x %= 3
print("x %= 3 →", x)
x **= 2
print("x **= 2 →", x)

print("\n=== 3. Comparison (Relational) Operators ===")
a = 5
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= 5:", a >= 5)
print("b <= 10:", b <= 10)

print("\n=== 4. Logical Operators ===")
a = 5
b = 10
print("a > 3 and b > 5:", a > 3 and b > 5)
print("a < 3 or b > 5:", a < 3 or b > 5)
print("not(a > 3):", not(a > 3))

print("\n=== 5. Bitwise Operators ===")
a = 5  # 0101
b = 3  # 0011
print("a & b =", a & b)  # AND
print("a | b =", a | b)  # OR
print("a ^ b =", a ^ b)  # XOR
print("~a =", ~a)        # NOT
print("a << 1 =", a << 1) # Left Shift
print("a >> 1 =", a >> 1) # Right Shift

print("\n=== 6. Identity Operators ===")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)     # True
print("x is z:", x is z)     # False
print("x is not z:", x is not z) # True

print("\n=== 7. Membership Operators ===")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)
print("6 not in my_list:", 6 not in my_list)
