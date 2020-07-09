class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        ans = []
        queue = collections.deque() # keeps track of the largest num's idx
        
        for i in range(len(nums)):
            if queue and queue[0] <= i-k:
                queue.popleft()
                
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
                
            queue.append(i)
            if i >= k-1:
                ans.append(nums[queue[0]])
                
        return ans