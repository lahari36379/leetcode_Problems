class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel_count=0
        left=0
        c=0
        for right in range(len(s)):
            if s[right] in "aeiou":
                c+=1
            if right>=k-1:
                max_vowel_count=max(max_vowel_count,c)
                if s[left] in "aeiou":
                    c-=1
                left+=1
        return max_vowel_count           

        