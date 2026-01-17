class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mapper = {} 
        maxf = 0
        for i in nums:
            mapper[i] = mapper.get(i,0) + 1
            maxf = max(maxf, mapper[i])
        return sum(v for i,v in mapper.items() if v == maxf)