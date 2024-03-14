
def findFactorialIterative(number: int) -> int:
    mul = 1
    i = number
    while i > 0:
        mul *= i
        i -= 1
    return mul

# Done by me
# def findFactorialRecursive(number: int, mul:int) -> int:
#     mul *= number
#     if number == 1:
#         return mul
#     number -= 1
#     return findFactorialRecursive(number, mul)

# Better version
def findFactorialRecursive(number: int) -> int:
    if number == 2:
        return 2
    return number*findFactorialRecursive(number-1)

def main():
    # print(findFactorialIterative(10))
    # mul = 1
    print(findFactorialRecursive(10))

    # Iterative and recursive, both have O(n) time complexity.

if __name__ == "__main__":
    main()