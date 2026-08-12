class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        for i in s1:
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        left=0
        d2={}
        for right in range(len(s2)):
            if s2[right] in d2.keys():
                d2[s2[right]]+=1
            else:
                d2[s2[right]]=1
            if right>=len(s1)-1:
                if d1==d2:
                    return True
                    break
                d2[s2[left]]-=1
                if d2[s2[left]]==0:
                    d2.pop(s2[left])
                left+=1
        return False                 

        