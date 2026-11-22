class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2,3,6,2,4]
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap)>1:
            largest = heapq.heappop_max(max_heap)
            second = heapq.heappop_max(max_heap)

            if largest > second:
                heapq.heappush_max(max_heap, largest-second)
        return (heapq.heappop(max_heap) if max_heap else 0)