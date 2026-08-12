class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        left=0
        max_sum=0
        sum_=0
        for right in range(len(nums)):
            if nums[right] in d.keys():
                d[nums[right]]+=1
            else:
                d[nums[right]]=1
            sum_+=nums[right]    
            if right>=k-1:
                if len(d)==k:
                    max_sum=max(max_sum,sum_)
                d[nums[left]]-=1
                sum_-=nums[left]
                if d[nums[left]]==0:
                    d.pop(nums[left])
                left+=1
        return max_sum                
            


        