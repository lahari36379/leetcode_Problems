class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d2={}
        for i in p:
            if i in d2.keys():
                d2[i]+=1
            else:
                d2[i]=1
        left=0
        d1={}
        lst=[]
        for right in range(len(s)):
            if s[right] in d1.keys():
                d1[s[right]]+=1
            else:
                d1[s[right]]=1
            if right>=len(p)-1:
                if d1==d2:
                    lst.append(left)
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left+=1
        return lst                


        