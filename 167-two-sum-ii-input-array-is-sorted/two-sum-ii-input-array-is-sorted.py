class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        left=0
        right=len(numbers)-1
        while left<right:
            sum_=numbers[left]+numbers[right]
            if sum_<target:
                left+=1
            elif sum_>target:
                right-=1
            else:
                output.append(left+1)
                output.append(right+1) 
                break
        return output               
       