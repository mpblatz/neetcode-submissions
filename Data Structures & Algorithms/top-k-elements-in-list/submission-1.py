class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nf = {}
        for n in nums:
            nf[n] = nf.get(n, 0) + 1

        lf = [[] for _ in range(len(nums) + 1)]
        for n in nf:
            lf[nf[n]].append(n)

        res = []
        for bucket in reversed(lf):
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res
