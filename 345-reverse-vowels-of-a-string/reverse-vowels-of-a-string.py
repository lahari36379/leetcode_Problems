def vowel(i):
    if i in "aeiouAEIOU":
        return True
    else:
        return False    
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)   
        left=0
        right=len(s)-1
        while left<right:
            if vowel(s[left]) and vowel(s[right]):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif vowel(s[left]):
                right-=1
            elif vowel(s[right]):
                left+=1
            else:
                left+=1
                right-=1
        return ''.join(s)                  


        