class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        current_sum=0
        left=0
        for right in range(len(arr)):
            current_sum+=arr[right]
            if right>=k-1:
                avg=current_sum/k
                if avg>=threshold:
                    count+=1
                current_sum-=arr[left]
                left+=1
        return count 

        