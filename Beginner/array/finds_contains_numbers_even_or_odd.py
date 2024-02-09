import time
import resource

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            num_digits = 0
            while num > 0:
                num //= 10
                num_digits += 1
            if num_digits % 2 == 0:
                count += 1
        return count

# Create an instance of the Solution class
solution = Solution()

# Your input data
nums = [14, 556, 1, 666, 45]

# Measure execution time
start_time = time.time()

# Measure memory usage
start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Call the method
result = solution.findNumbers(nums)

# Calculate execution time
execution_time = time.time() - start_time

# Calculate memory usage
memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - start_memory

# Print results
print("Count of numbers with even number of digits:", result)
print("Runtime: {:.3f} ms".format(execution_time * 1000))
print("Memory Usage: {:.1f} MB".format(memory_usage / 1024))
