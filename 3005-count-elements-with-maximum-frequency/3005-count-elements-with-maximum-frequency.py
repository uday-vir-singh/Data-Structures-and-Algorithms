class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        count = 0
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i]=1
        # values = list(d.values())
        # maxFrequency = max(values)
        return sum(freq for freq in d.values() if freq == max(d.values()))