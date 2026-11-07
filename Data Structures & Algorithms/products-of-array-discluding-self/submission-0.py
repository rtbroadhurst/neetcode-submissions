class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total_product *= num

        if zeros > 1:
            return [0] * len(nums)

        if zeros == 1:
            return [total_product if num == 0 else 0 for num in nums]

        return [total_product // num for num in nums]