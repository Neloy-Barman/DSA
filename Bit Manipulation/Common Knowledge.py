# Converting a decimal to binary 
# Positive number
dec = 85
pbin = bin(dec)
print(f"Binary of {dec} is: {pbin}")

# Negative number
dec = -85
nbin = bin(dec)
print(int(nbin, 2))
print(f"Binary of {dec} is: {nbin}")


# Converting a binary to decimal
# Positive number
pbin = "0b01100110"
dec = int(f"{pbin}", 2)
print(f"Decimal of {pbin} is: {dec}")

# Negative number
nbin = "-0b01100110"
dec = int(f"{nbin}", 2)
print(f"Decimal of {nbin} is: {dec}")


# Negation of a number
nbin = 0b01100110
neg = ~nbin
print(f"Negation of {nbin}: {neg}")
print(f"Binary of {neg}: {bin(neg)}")


