class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        numZeroes = 0
        for n in nums:
            if n == 0:
                numZeroes += 1
            else:
                totalProduct *= n
        res = []
        for n in nums:
            if numZeroes > 1:
                res.append(0)
            elif numZeroes == 1:
                if n == 0:
                    res.append(totalProduct)
                else:
                    res.append(0)
            else:
                res.append(totalProduct // n)
        return res