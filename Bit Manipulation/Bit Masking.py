# # Bit masking 
# x = 0b00000000 # The number 0 in binary 
# # We want to set the 3rd and 5th bits of x.
# mask = 0b00101000
# x = x | mask
# print(f"After masking: {x}") 


# # Bit masking 
# x = 0b11111111 # The number 255 in binary 
# # We want to set the 4th and 6th bits of x.
# mask = 0b10101111
# x = x & mask
# print(f"After masking: {x}") 

# x = 0b11010111  # The number 215 in binary
# mask = 0b10000000  # The mask with the seventh bit set to 1
# if x & mask:
#     print("The seventh bit is set to 1")
# else:
#     print("The seventh bit is not set to 1")

# print(x)
# print(~x)

print(f"Binary of 215: {bin(215)}")
print(f"Binary of -215: {bin(-215)}")

x = int("-0b11010111", 2)
print(x)