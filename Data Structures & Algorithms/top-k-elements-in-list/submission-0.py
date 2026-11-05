class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sample input [7,7,8,8,9]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # freq => { 7:2, 8:2, 9:1 }
        arr = [[] for _ in range(len(nums) + 1)]
        for n, c in freq.items():
            arr[c].append(n)
        # arr => [ [], [9], [7,8] ]
        res = []
        for i in reversed(range(len(arr))):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res