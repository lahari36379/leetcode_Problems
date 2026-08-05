class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        max_count=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                if count>max_count:
                    max_count=count
                count=1
        return max(max_count,count)            

        