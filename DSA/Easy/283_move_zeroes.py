# Problem: Move Zeroes
# LeetCode: 283
# Difficulty: Easy
# Approach: Two-pointer technique to shift non-zero elements forward
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
