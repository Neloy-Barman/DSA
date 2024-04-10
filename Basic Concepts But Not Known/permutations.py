

def findPermutations(array: list[str], stack: list[str], permutations: list[list[str]]):
    if not array:
        permutations.append("".join(stack))
        return stack, permutations
    for i in range(len(array)):
        stack.append(array[i])
        stack, permutations = findPermutations(array=[array[j] for j in range(len(array)) if j != i], stack=stack, permutations=permutations)
        stack.pop()
    return stack, permutations


def main():
    ls = ["A", "B", "C"]
    _, permutations = findPermutations(array=ls, stack=[], permutations=[])
    print(permutations) 

if __name__ == "__main__":
    main()