class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        total = 1
        for num in nums:
            output.append(total)
            total *= num

        total = 1
        for index, num in reversed(list(enumerate(nums))):
            output[index] *= total 
            total *= num

        return output


        
