class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        return -heap[0]