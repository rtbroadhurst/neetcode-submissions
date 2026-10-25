import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))
                    
        return [num for _, num in heap]