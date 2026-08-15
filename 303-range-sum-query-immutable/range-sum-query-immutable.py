class NumArray:
    def __init__(self, nums: List[int]):
        self.nums=nums
    def sumRange(self, left: int, right: int) -> int:
        sum_=0
        new_list=[]
        for i in self.nums:
            sum_+=i
            new_list.append(sum_)
        for i in range(len(self.nums)):
            if left==0:
                return new_list[right]
            else:
                return new_list[right]-new_list[left-1]    

        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)