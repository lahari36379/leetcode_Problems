class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_array=[0]
        sum_=0
        for i in range(len(nums)):
            sum_+=nums[i]
            prefix_array.append(sum_)     
        for i in range(len(nums)):
            left_sum=prefix_array[i]
            right_sum=prefix_array[len(nums)]-prefix_array[i+1]
            if left_sum==right_sum:
                return i
        return -1        


        