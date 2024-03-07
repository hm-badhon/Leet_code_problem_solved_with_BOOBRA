class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        dlp =[]
        for i in arr:
            dlp.append(i)
            if i == 0:
                dlp.append(0)
        arr[:] = dlp[:len(arr)]
            
solution = Solution()
arr = [1,0,2,3,0,4,5,0]

result = solution.duplicateZeros(arr)
print(arr)