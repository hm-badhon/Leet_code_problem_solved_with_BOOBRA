class Solution(object):
    def merge(self,nums1,m,nums2,n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        print(nums1)
     
        
        return nums1.sort()


solution = Solution()
nums1 = [56,1,4,0,0]
nums2 = [25,2,5,6]


m= len(nums1)
n= len(nums2)

result = solution.merge(nums1,m,nums2,n)
print('result ',result)