class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (distance,x,y))

        ans = []
        for i in range(k):
            closest = heapq.heappop(minHeap)
            ans.append([closest[1], closest[2]])

        return ans

