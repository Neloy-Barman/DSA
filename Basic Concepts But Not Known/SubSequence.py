
def findSubSequences(array: str, stack: list[str], subSequences: list[str]):
    if not array:
        return stack, subSequences
    for i in range(len(array)):
        stack.append(array[i])
        subSequences.append("".join([n for n in stack]))
        stack, subSequences = findSubSequences(array=array[i+1:], stack=stack, subSequences=subSequences)
        stack.pop()
    return stack, subSequences


def main():
    array = ["a", "b", "c", "d"]
    _, subSequences = findSubSequences(array=array, stack=[], subSequences=[""])
    print(subSequences)

if __name__ == "__main__":
    main()