class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average=-10000
        left=0
        current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            if right>=k-1:
                avg=current_sum/k
                if avg>max_average:
                    max_average=avg
                current_sum-=nums[left]
                left+=1
        return max_average            
        