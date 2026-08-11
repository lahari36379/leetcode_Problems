class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        max_sum = 0
        d = {}  
        for right in range(len(nums)):
            d[nums[right]] = d.get(nums[right],0)+1
            current_sum += nums[right]
            if right >= k-1:
                if len(d)== k:
                    max_sum = max(max_sum,current_sum)
                d[nums[left]] -= 1
                current_sum -= nums[left]
                if d[nums[left]] == 0:
                    d.pop(nums[left])
                left += 1
        return max_sum