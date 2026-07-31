class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output=set()
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_>0:
                    right-=1
                elif sum_<0:
                    left+=1
                else:
                    triplet= (nums[i],nums[left],nums[right])
                    a=sorted(triplet)
                    output.add(tuple(a))
                    left+=1
                    right-=1           
        return list(output)           

                 
  


            