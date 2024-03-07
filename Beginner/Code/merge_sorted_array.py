class Solution(object):
    def merge(self,merge_list):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        list= []
        print(nums1)
        for i in merge_list:
            if i == 0:
                continue
            else:
                list.append(i)
        return sorted(list)



solution = Solution()
nums1 = [0]
nums2 = [25,2,5,6]
# merge_list = nums1.extend(nums2)
merge_list = nums1+nums2
print(merge_list)
m= len(nums1)
n= len(nums2)

result = solution.merge(merge_list)
print('result ',result)