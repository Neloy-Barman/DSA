


# def allSubsequences(nums: list[int]):
#     totalLoops = len(nums)
#     seqLength = totalLoops
#     while seqLength >= 1:
#         print(f"Loop number: {seqLength}")
#         j = 0
#         temp = nums[j:seqLength-1]
#         # print(f"Base element: {temp}")
#         k = seqLength-1
#         # print(f"This is moving index: {k}")
#         while k < totalLoops:
#             # print(f"This is last moving index: {k}")
#             temp2 = [a for a in temp]
#             temp2.append(nums[k])
#             print(f"These are elements: {temp2}")
#             k += 1
#         seqLength -= 1


# def allSubsequences2(nums: list[int]):
#     totalelems = len(nums)
#     seqLength = totalelems
#     while seqLength > 0:
#         print(f"This is sequence length: {seqLength}")
#         j = 0
#         while j < totalelems - (seqLength-1):
#             # print(f"Start moving index: {j}")
#             temp = nums[j:j+seqLength-1]
#             # print(f"Base element: {temp}")
#             k = j+seqLength-1
#             # print(f"Last moving index: {k}")
#             if k == j:
#                 print(f"These are elements: {[nums[k]]}")
#             else:
#                 while k < totalelems:
#                     temp2 = [a for a in temp]
#                     temp2.append(nums[k])
#                     print(f"These are elements: {temp2}")
#                     k += 1
#             j += 1
#         seqLength -= 1



# def Subsequences(nums: list[int]):
#     totalelems = len(nums)
#     seqLength = totalelems
#     sequences = []
#     while seqLength > 0:
#         j = 0
#         while j < totalelems - (seqLength-1):
#             k = j + seqLength - 1
#             temp = nums[j:k]
#             if k == j:
#                 string = "".join([nums[k]])
#                 if string not in sequences:
#                     sequences.append(string)
#             else:
#                 while k < totalelems:
#                     temp2 = [a for a in temp]
#                     temp2.append(nums[k])
#                     string = "".join(temp2)
#                     if string not in sequences:
#                         sequences.append(string)
#                     k += 1
#             j += 1
#         seqLength -= 1
#     return sequences







# def subsequences(array: list):
#     totalElems = len(array)
#     seqLength = totalElems
#     subs = []
#     while seqLength > 0:
#         j = 0
#         while j < totalElems - (seqLength-1):
#             k = j+seqLength-1
#             temp = array[j:k]
#             if k == j:
#                 string = "".join([array[k]])
#                 if string not in subs:
#                     subs.append(string)
#             else:
#                 while k < totalElems:
#                     temp2 = [n for n in temp]
#                     temp2.append(array[k])
#                     string = "".join(temp2)
#                     if string not in subs:
#                         subs.append(string)
#                     k += 1
#             j += 1
#         seqLength -= 1
#     return subs
















# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         totalElems = len(t)
#         seqLength = len(s)
#         j = 0
#         while j < totalElems - (seqLength-1):
#             k = j+seqLength-1
#             temp = t[j:k]
#             while k < totalElems:
#                 print(temp+t[k])
#                 if temp+t[k] == s:
#                     return True
#                 k += 1
#             j += 1
#         return False



# def main():



#     nums = ['a', 'b', 'c', 'd']
#     # allSubsequences2(nums)

#     # string =[ c for c in "geeks"]
#     subs = subsequences([ c for c in "geeks"])
#     print(subs)

#     # string = "methionylthreonylthreonylglutaminylalanyl"
#     # subs = Subsequences([c for c in string])
#     # print(subs)

#     # x = "abcd"
#     # y = x
#     # y += "dfds"
#     # print(x)
#     # print(y)

#     s = "abc"
#     t = "ahbgdc"
#     Solution().isSubsequence(s=s, t = t)

    


# if __name__ == "__main__":
#     main()





