class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        numSet = set(nums)
        longest = 1
        for n in numSet:
            if n - 1 not in numSet:    
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
