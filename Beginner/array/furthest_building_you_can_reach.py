class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        import heapq
        
        diffs = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(diffs, diff)
                if len(diffs) > ladders:
                    bricks -= heapq.heappop(diffs)
                if bricks < 0:
                    return i
        return len(heights) - 1

# Test the Solution class
solution = Solution()

# Example 1
heights1 = [4, 2, 7, 6, 9, 14, 12]
bricks1 = 5
ladders1 = 1
print(solution.furthestBuilding(heights1, bricks1, ladders1))  # Output: 4

# Example 2
heights2 = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks2 = 10
ladders2 = 2
print(solution.furthestBuilding(heights2, bricks2, ladders2))  # Output: 7

# Example 3
heights3 = [14, 3, 19, 3]
bricks3 = 17
ladders3 = 0
print(solution.furthestBuilding(heights3, bricks3, ladders3))  # Output: 3
