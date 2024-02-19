from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        counts = Counter(arr)
        print('counts---',counts)


        unique_integers = len(counts)
        print('unique_integers',unique_integers)
        removals = sorted(counts.values())

        keys = counts.items()
        keys = counts.keys()

        print('keys',keys)
        print('removals :',removals)
        
        for count in removals:
            if k >= count:
                k -= count
                unique_integers -= 1
            else:
                break
        
        return unique_integers

# Example usage:
sol = Solution()
# arr1 = [5, 5, 4]
# k1 = 1
# print(sol.findLeastNumOfUniqueInts(arr1, k1))  # Output: 1

# arr2 = [4, 3, 1, 1, 3, 3, 2]
# k2 = 3
# print(sol.findLeastNumOfUniqueInts(arr2, k2))  # Output: 2


arr = [5, 3, 1, 1, 3, 3, 2]
k2 = 3
print(sol.findLeastNumOfUniqueInts(arr, k2))  # Output: 2