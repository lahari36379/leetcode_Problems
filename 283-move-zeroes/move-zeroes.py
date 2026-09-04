class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst=[]
        for i in nums:
            if i !=0:
                lst.append(i)
        zeroes=len(nums)-len(lst)
        lst+=[0]*zeroes
        nums[:]=lst        