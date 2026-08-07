class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lst=[]
        d2={}#Compute the frequencies of string p
        for i in p:
            d2[i]=d2.get(i,0)+1
        d1={}#Do a k-length sliding window on s
        left=0   #count the frequencies of characters in substring into d1 
        for  right in range(len(s)):
            d1[s[right]]=d1.get(s[right],0)+1 #counting frequencies of sub string k
            if right>=len(p)-1: #checking the validity of window
                if d1==d2:#comparing hashmaps to check anagrams adding start index to ans
                #removing the outgoing element-left
                    lst.append(left)
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    d1.pop(s[left])     
                left+=1
        return lst                

