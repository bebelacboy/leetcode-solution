from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, 0)]
        heights.append(-1)
        max_area = 0
        for i in range(len(heights)):
            if heights[i] > stack[-1][0]:
                stack.append((heights[i], 1))
                continue
            step = 0
            while len(stack) > 0 and heights[i] <= stack[-1][0]:
                popped = stack.pop()
                step += popped[1]
                max_area = max(max_area, popped[0] * step)
            stack.append((heights[i], step + 1))
        return max_area
                
                

print(Solution().largestRectangleArea([2, 1, 2]))