
def decimalToBinary(number: int, base: int, stack: list[int]):
    if number < 2:
        stack.append(f"{number}")
        return stack[::-1]
    quotient = number // base
    remainder = number % base
    stack.append(f"{remainder}")
    stack = decimalToBinary(number=quotient, base=base, stack=stack)
    return stack

def binaryToDecimal(number: str) -> int:
    i = len(number)-1
    p = 0
    sum = 0
    while p < len(number):
        sum += int(number[p])*pow(2, i)
        i -= 1
        p += 1
    return sum

def main():
    base = 2

    number = 21
    stack = decimalToBinary(number=number, base=base, stack=[]) 
    bin = "".join(stack)
    print(f"Binary of {number}: {bin}")

    # number = 50 
    # stack = decimalToBinary(number=number, base=base, stack=[]) 
    # bin = "".join(stack)
    # print(f"Binary of {number}: {bin}")


    # number = 50103 
    # stack = decimalToBinary(number=number, base=base, stack=[]) 
    # bin = "".join(stack)
    # print(f"Binary of {number}: {bin}")

    # number = "11"
    # number = "1010"
    number = "10101"
    dec = binaryToDecimal(number=number)
    print(f"Decimal of {number}: {dec}")

if __name__ == "__main__":
    main()