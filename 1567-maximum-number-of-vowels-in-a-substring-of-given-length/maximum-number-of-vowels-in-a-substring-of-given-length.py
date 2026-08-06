class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        cnt=0
        max_vowel_count=0
        for right in range(len(s)):
            if s[right] in "aeiou":
                cnt+=1
            if right>=k-1:
                if cnt>max_vowel_count:
                    max_vowel_count=cnt
                if s[left] in "aeiou":
                     cnt-=1
                left+=1
        return max_vowel_count            

        