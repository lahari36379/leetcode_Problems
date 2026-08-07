class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        for i in range(len(s1)):
            d1[s1[i]]=d1.get(s1[i],0)+1
        d2={}
        left=0
        for right in range(len(s2)):
            d2[s2[right]]=d2.get(s2[right],0)+1
            if right>=len(s1)-1:
                if d1==d2:
                    return True
                    break
                d2[s2[left]]-=1
                if d2[s2[left]]==0:
                    d2.pop(s2[left])
                left+=1
        return False                

        