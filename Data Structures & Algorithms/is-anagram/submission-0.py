class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1

        for letter in t:
            counts[letter] = counts.get(letter, 0) - 1
            if counts[letter] < 0:
                return False

        return True