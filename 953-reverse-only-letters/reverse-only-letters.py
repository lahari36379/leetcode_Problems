class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            if ((s[left]>='A' and s[left]<='Z') or (s[left]>='a' and s[left]<='z')) and((s[right]>='A' and s[right]<='Z') or (s[right]>='a' and s[right]<='z'))  :
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif (s[left]>='A' and s[left]<='Z') or (s[left]>='a' and s[left]<='z'):
                right-=1
            elif  (s[right]>='A' and s[right]<='Z') or (s[right]>='a' and s[right]<='z'):
                left+=1
            else:
                left+=1
                right-=1
        return ''.join(s)              
