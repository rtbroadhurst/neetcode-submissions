class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for num in nums:
            seen.add(num)

        for num in seen:
            length = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    length += 1
                    num +=1 
            if longest < length:
                longest = length

        
        return longest

                



