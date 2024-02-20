class Solution(object):
    def missingNumber(self, numbers):
        """
        :type nums: List[int]
        :rtype: int
        """
        lengh_n = len(numbers)
        # print('length ---',lengh_n)
        missing_value = []
        for i in range(lengh_n+1):
            # missing_value.append(i)
            if i in numbers:
                continue
            else:
                missing_value.append(i)
        return missing_value[0]
        
solution = Solution()

# numbers=  [0,1]
numbers = [9,6,4,2,3,5,7,0,1]
# numbers= [3,0,1]


result = solution.missingNumber(numbers)

# print('missing value in result : ',result)
print(result)