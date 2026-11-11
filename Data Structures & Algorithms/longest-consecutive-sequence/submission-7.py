class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        seq = 0
        res = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] - nums[i - 1] == 1:
                seq += 1
            else:
                seq = 1
            res = max(res, seq)
        return res
