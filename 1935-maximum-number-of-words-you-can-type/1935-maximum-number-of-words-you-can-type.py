class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        canbetyped = True
        for i in text.split():
            for j in brokenLetters:
                if j in i:
                    canbetyped = False
            if canbetyped == True:
                count += 1
            else:
                canbetyped = True
        return count