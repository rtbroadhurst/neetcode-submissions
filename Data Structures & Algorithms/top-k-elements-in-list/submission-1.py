class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        count_num = {}
        for num, count in num_count.items():
            if count not in count_num:
                count_num[count] = []
            count_num[count].append(num)

        top_k = []
        for count in range(len(nums), 0, -1):
            for num in count_num.get(count, []):
                top_k.append(num)
            if len(top_k) == k:
                return top_k

        


