class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #vowel_count=0
        max_vowel_count=0
        left=0
        lst=[]
        c=0
        for right in range(len(list((s)))):
            lst.append(s[right])
            if s[right] in "aeiou":
                c+=1
            if right>=k-1:
                max_vowel_count=max(max_vowel_count,c)
                if s[left] in "aeiou":
                    c-=1
                left+=1
        return max_vowel_count           

        