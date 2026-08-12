class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while  j<len(s) and i<len(t):
                if t[i]==s[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
        if j==len(s):
            return True
        else:
            return False                


            




        