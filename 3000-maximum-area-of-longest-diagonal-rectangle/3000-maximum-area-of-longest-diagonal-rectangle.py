import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonals = []
        for i in dimensions:
            l = i[0]
            b = i[1]
            diagonals.append(math.sqrt(l*l + b*b))
        maxdiagonal = max(diagonals)
        area = []
        for i in range(len(diagonals)):
            if diagonals[i] == maxdiagonal:
                area.append(dimensions[i][0]*dimensions[i][1])
        return max(area)