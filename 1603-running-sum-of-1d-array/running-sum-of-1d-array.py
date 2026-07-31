class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_lst=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            new_lst.append(sum)
        return new_lst    