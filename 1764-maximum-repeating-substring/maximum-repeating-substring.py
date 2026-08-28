class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count=0
        repeated=""
        while repeated+word in sequence:
            count+=1
            repeated+=word
        return count    
           

        
        