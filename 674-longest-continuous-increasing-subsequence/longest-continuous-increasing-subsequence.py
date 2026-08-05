class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=1
        max_count=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                if count>max_count:
                    max_count=count
                count=1
        return max(max_count,count)            
        