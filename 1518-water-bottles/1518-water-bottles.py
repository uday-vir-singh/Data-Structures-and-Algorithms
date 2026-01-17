class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numDrink = 0
        while numBottles >= numExchange:
            numDrink += numExchange
            numBottles = numBottles - numExchange + 1
        else:
            numDrink += numBottles
        return numDrink