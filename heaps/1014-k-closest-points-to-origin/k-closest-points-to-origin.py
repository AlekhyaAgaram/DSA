class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)
            heapq.heappush(heap, (dist, point))
        
        res = []
        while k > 0 and heap:
            dist, point = heapq.heappop(heap)
            res.append(point)
            k -= 1
        return res