# Problem: Next Greater Element I
# LeetCode: 496
# Difficulty: Easy
# Approach: Use stack + hashmap to find next greater elements
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]
