class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tp = 1
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else: 
                tp *= n
        res = []
        for n in nums:
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                res.append(tp if n == 0 else 0)
            else:
                res.append(tp // n)
        return res
