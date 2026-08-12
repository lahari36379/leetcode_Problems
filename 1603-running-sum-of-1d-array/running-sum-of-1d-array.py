class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_lst=[]
        sum_=0
        for i in range(len(nums)):
            sum_+=nums[i]
            new_lst.append(sum_)
        return new_lst    
        