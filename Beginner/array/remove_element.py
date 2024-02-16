# class Solution(object):
#     def removeElement(self, nums , val):
#         lists=[]
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 # lists.append(nums[i])
#                 continue
#             else:
#                 lists.append(nums[i])
#                 # lists.append("_")
#         print(lists)
#         return len(lists)
# solution = Solution()
# nums = [3,2,2,3]
# val = 3

# result = solution.removeElement(nums,val)
# # print('result',result)
# print(result)


class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a pointer to keep track of the index where non-matching elements should be placed
        pointer = 0
        
        # Iterate through the list
        for i in range(len(nums)):
            # If the current element is not equal to the value to be removed
            if nums[i] != val:
                # Move the non-matching element to the position indicated by the pointer
                nums[pointer] = nums[i]
                # Move the pointer to the next position
                pointer += 1
        print(pointer)
        print(nums)
        # Return the modified list containing only non-matching elements
        return nums[:pointer]

solution = Solution()
nums = [3, 2, 2, 3]
val = 3

result = solution.removeElement(nums, val)
print(result)  # This will print the modified list
