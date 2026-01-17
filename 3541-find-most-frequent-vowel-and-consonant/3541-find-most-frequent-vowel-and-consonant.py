class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        vd = {}
        cd = {}
        for i in s:
            if i in vowels:
                vd[i] = vd.get(i,0) + 1
            else:
                cd[i] = cd.get(i,0) + 1
        return max(vd.values(), default = 0) + max(cd.values(), default = 0)