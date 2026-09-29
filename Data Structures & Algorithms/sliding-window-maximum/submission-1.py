class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = 0 
        q = deque() #indices of useful max candidates
        result = [] #max # from each window

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]: #Go to the last index stored in the deque, then look up its value in nums
                q.pop()
            q.append(r)

            if q and q[0] < l:
                q.popleft()

            if r - l + 1 == k: 
                result.append(nums[q[0]])
                l += 1 #gets moved once a we form a complete window of size k 
            r += 1
    
        return result
        