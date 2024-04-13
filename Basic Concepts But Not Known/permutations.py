

# Mine
# def findPermutations(array: list[str], stack: list[str], permutations: list[list[str]]):
#     if not array:
#         permutations.append("".join(stack))
#         return stack, permutations
#     for i in range(len(array)):
#         stack.append(array[i])
#         stack, permutations = findPermutations(array=[array[j] for j in range(len(array)) if j != i], stack=stack, permutations=permutations)
#         stack.pop()
#     return stack, permutations


# Neetcode
def findPermutations(array: list):
    results = [] 
    if len(array) == 1:
        return [array[:]]
    for i in range(len(array)):
        n = array.pop(0)
        perms = findPermutations(array=array)
        for perm in perms:
            perm.append(n)
        results.extend(perms)
        array.append(n)
    return results 


def main():

    # array = [1, 2, 3]
    perms = findPermutations(array=ls)
    print(perms)

if __name__ == "__main__":
    main()