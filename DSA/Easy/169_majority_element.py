# Problem: Majority Element
# LeetCode: 169
# Difficulty: Easy
# Approach: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
