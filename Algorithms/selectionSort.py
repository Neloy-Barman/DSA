
def SelectionSort(nums: list[int]) -> list[int]:
    i = 0 
    while i < len(nums):
        min_ = i
        j = i+1
        while j < len(nums):
            if nums[j] < nums[min_]:
                min_  = j
            j += 1
        temp = nums[i]
        nums[i] = nums[min_]
        nums[min_] = temp
        i += 1
    return nums


def main():
    # nums = [6,5,3,1,8,7,2,4]
    nums = [99,44,6,2,1,5,63,87,283,4,0]
    print(SelectionSort(nums=nums))

if  __name__ == "__main__":
    main()