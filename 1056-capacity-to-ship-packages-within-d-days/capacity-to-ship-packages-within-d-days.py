def canship(weights,days,capacity):
    days_needed=1
    weight_capacity=0
    for weight in weights:
       # weight_capacity+=weight
        if weight_capacity+weight<=capacity:
            weight_capacity+=weight
        else:
            days_needed+=1
            weight_capacity=weight
    if days_needed<=days:
        return True
    else:
        return False              
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canship(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low            