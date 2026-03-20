# Problem: Rotate Array
# LeetCode: 189
# Difficulty: Medium
# Approach: Reverse parts of array
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
