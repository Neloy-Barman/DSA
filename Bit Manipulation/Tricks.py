# Isolation of the right-most set bit
x = 0b01010101  # The number 85 in binary
y = x & (-x) # The result is 0b00000001, or 1 in decimal
print(f"After isolating the set bit: {y}")

# Clearing the right-most set bit
x = 0b01010101  # The number 85 in binary
y = x & (x - 1)  # The result is 0b01010100, or 84 in decimal
print(f"After clearing the set bit: {y}")

# Counting the number of 1-bits
x = 0b01010101  
count = 0
while x:
    count += 1
    x &= (x-1)
print(count)

# Checking if a number is odd or even
x = 10  # The number 10 is even
if x & 1:
    print("x is odd")
else:
    print("x is even")

x = 11  # The number 11 is odd
if x & 1:
    print("x is odd")
else:
    print("x is even")

# Determining the signs of a number
x = 10  # The number 10 is positive
print(x >> 31)
if x >> 31:
    print("x is negative")
else:
    print("x is positive")

x = -10  # The number -10 is negative
print(x >> 31)
if x >> 31:
    print("x is negative")
else:
    print("x is positive")


# https://dev.to/anurag629/the-power-of-bit-manipulation-how-to-solve-problems-efficiently-3p1h