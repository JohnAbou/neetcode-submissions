class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in nums:
            maxHeap.append(-i)

        heapq.heapify(maxHeap)

        for i in range(k):
            largest = heapq.heappop(maxHeap)

        return -largest
