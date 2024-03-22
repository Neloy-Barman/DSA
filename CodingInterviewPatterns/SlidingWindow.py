
def slidingWindow(numbers: list[int], windowSize: int):    
    # Finding Maximum sum of subarray with a fixed windowsize
    i, maxSum = 0, 0
    while i+windowSize <= len(numbers):
        sum = 0
        for j in range(i, i+windowSize):
            sum += numbers[j]
        if sum > maxSum:
            maxSum = sum
        i += 1
    return maxSum


def main():
    numbers = [2,1,5,1,3,2]
    maxSum = slidingWindow(numbers=numbers, windowSize=2)
    print(f"The maximum sum is: {maxSum}")

if __name__ == "__main__":
    main()










