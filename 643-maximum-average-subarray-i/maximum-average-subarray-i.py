class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window(fixed-length sliding window)
        maxaverage=-10000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right>=k-1:
                avg=currentsum/k
                maxaverage=max(avg,maxaverage)
                #subtracting the value on left(window size is exceed k)
                currentsum-=nums[left]
                left+=1
        return maxaverage        

        