

# def backTracking(nums, i, permutations):
#     permutations.append([nums[i]])
#     i += 1
#     if i < len(nums):
#         backTracking(nums, i, permutations)
#     return permutations

def multiplicationCheck(nums, target) -> bool:
    mul = 1
    for num in nums:
        mul *= num
    if mul < target:
        return True
    return False

def contiguous(nums, match: list):
    if len(nums) > 1:
        if match.index(nums[1]) != match.index(nums[0])+1:
            return False
    return True 

def backTracking(nums, permutations, target) -> int:
    i = 0
    while i < len(nums):      
        temp = [nums[j] for j in range(len(nums)) if j != i]
        if temp != []:
            if temp not in permutations:
                permutations.append(temp)
            backTracking(temp, permutations=permutations, target=target)
        i += 1
    return permutations



def main():
    # nums = [1, 2, 3]
    # # nums = [10, 5, 2, 6]
    # permutations = [nums]
    # # permutations = backTracking(nums=nums, i=0, permutations=permutations)
    # # print(permutations)
    # permutations = backTracking(nums=nums, permutations=permutations, target=100)
    # print(permutations)

    # permutations = [tation for tation in permutations if contiguous(tation, nums)]
    # print(permutations)
    
    # counter = 0
    # i = 0
    # while i < len(permutations):
    #     if multiplicationCheck(permutations[i], target=0):
    #         counter += 1
    #     i += 1
    # print(counter)


    nums = [1,2,3]
    nums = [10,5,2,6,7]
    permutations = contiguousSubArrays(nums=nums)
    print(permutations)




# def countiguousSubArrays(nums, permutations):
#     totalLoops = len(nums)
#     i = 0
#     permutations = []
#     while totalLoops > 0:
#         while i <= totalLoops:
#             if nums[i:i+totalLoops]!= [] and nums[i:i+totalLoops] not in permutations:
#                 permutations.append(nums[i:i+totalLoops])
#             i += 1
#         print(permutations)
#         totalLoops -= 1
#         i = 0
#     print(permutations)

def productCheck(nums, target):
    mul = 1
    for num in nums:
        mul *= num
    print(f"Num: {nums}, Multiplication: {mul}")
    if mul < target:
        return True
    return False

def contiguousSubArrays(nums, k):
    totalLoops = 1
    j = len(nums)
    permutations = []
    i = 0
    while totalLoops <= len(nums):  
        k = 1
        while k <= j:
            permutations.append(nums[i:i+totalLoops])
            i += 1
            k += 1
        totalLoops += 1
        j -= 1
        i = 0 
    counter = 0
    for num in permutations:
        if productCheck(num, k):
            counter += 1
    print(counter)

    return permutations

if __name__ == "__main__":
    main()