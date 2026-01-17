class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count ={}
        high =0
        result =0

        for i in nums:
            if i in count:
                count[i]+=1
                
            else:
                
                count[i]=1


        for key in count:
            high = max(high,count[key])

        for key in count:
            if high ==count[key]:
                result +=high

        return result