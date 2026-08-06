class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        cnt=0
        min_operations=len(blocks)
        for right in range(len(blocks)):
            if blocks[right]=='W':
                cnt+=1
            if right>=k-1:
                if cnt<min_operations:
                    min_operations=cnt 
                if blocks[left]=='W':    
                     cnt-=1     
                left+=1
        return min_operations              

        