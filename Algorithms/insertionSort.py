
# def InsertionSort(nums: list[int]) -> list[int]:
#     i = 0
#     while  i < len(nums):
#         pivot = nums[i]
#         # print(f"Pivot Element: {pivot}, Before List: {nums[0:i]}")
#         for j in range(0,i):
#             if  pivot < nums[j]:
#                 # print(f"Pivot {pivot}, Changing index: {j}")
#                 # print('Here happens')
#                 temp = j
#                 k = i-1
#                 while k >= j:
#                     # x = nums[k+1]
#                     # print(f"Before k: {nums[k]}, k-1:{nums[k-1]}")
#                     nums[k+1] = nums[k]
#                     # print(f"After k: {nums[k]}, k+1:{nums[k-1]}")
#                     k -= 1
#                 # for k in range(j,i):
#                 #     nums[k+1]  = nums[k]
#                 nums[temp] = pivot
#                 # print(nums)
#                 break
#         # print("Hello World")
#         i += 1
#     return nums


def InsertionSort(nums: list[int]) -> list[int]:
    i = 0
    while  i < len(nums):
        pivot = nums[i]
        for j in range(0,i):
            if  pivot < nums[j]:
                temp = j
                k = i-1
                while k >= j:
                    nums[k+1] = nums[k]
                    k -= 1
                nums[temp] = pivot
                break
        i += 1
    return nums

def main():
    nums = [6,5,3,1,8,7,2,4]
    nums = [99,44,6,2,1,5,63,87,283,4,0]
    print(InsertionSort(nums=nums))

if __name__ == "__main__":
    main()