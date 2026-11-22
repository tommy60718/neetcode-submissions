class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            largest = heapq.heappop_max(max_heap)
            second = heapq.heappop_max(max_heap)

            if second < largest:
                heapq.heappush_max(max_heap, largest-second)
        return (heapq.heappop_max(max_heap) if max_heap else 0)