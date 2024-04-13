
# Operations

# And -> &
x = 0b10101010 # 170
y = 0b01010101 # 85 
z = x & y
print(f"Result of AND operation: {z}")

# Or -> |
x = 0b10101010  # 170
y = 0b01010101 # 85
z = x | y
print(f"Result of OR operation: {z}")

# XOR -> ^
x = 0b10101010  # 136
y = 0b01010101 # 85
z = x ^ y
print(f"Result of XOR operation: {z}")

x = 0b10001000  # 136
y = 0b01010101 # 85
z = x ^ y
print(f"Result of XOR operation: {z}")

# NOT -> ~
x = 0b10101010  # 170
y = ~x
print(f"Result of NOT operation: {y}")

# LEFT SHIFT -> <<
x = 0b10101010  # 170
y = x << 2
print(f"Result of operation: {y}")


# RIGHT SHIFT -> >>
x = 0b10101010  # 170
y = x >> 2
print(f"Result of operation: {y}")



