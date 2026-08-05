class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        max_count=0
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            else:
                if count>max_count:
                    max_count=count
                count=1
        return max(max_count,count)            

        