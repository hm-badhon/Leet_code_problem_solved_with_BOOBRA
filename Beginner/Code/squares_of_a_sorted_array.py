
class Solution(object):
    def sortedSquares(self, nums):
        sq =[]
        for i in nums:
            sq.append(i*i)
            print(sq)
        return sorted(sq)

solution = Solution()
nums = [-4,-1,0,3,10]
result =  solution.sortedSquares(nums)
print(result)