def fun(i):
    if (i>="a" and i<='z') or (i>='A' and i<='Z'):
        return True
    else:
        return False    
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if fun(s[left]) and fun(s[right]):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif fun(s[left]):
                right-=1
            elif fun(s[right]):
                left+=1
            else:
                left+=1
                right-=1
        return "".join(s)                    
        

         
        