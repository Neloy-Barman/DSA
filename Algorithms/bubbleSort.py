
def bubbleSort(nums: list[int]) -> list[int]:
    for i  in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums


def main():
    # nums = [6,5,3,1,8,7,2,4]
    nums = [99,44,6,2,1,5,63,87,283,4,0]
    print(bubbleSort(nums=nums))

if  __name__ == "__main__":
    main()