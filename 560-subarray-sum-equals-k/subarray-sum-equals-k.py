class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix+hashmap 
        csum=0 #current sum(this is our prefix sum)
        subcnt=0 #how many sub arrays we have seen with sum k
        seen={0:1} #hashmap tp store prefix sum found so far
        for i in nums:
            #compute prefix sum
            csum+=i
            #Required prefix sum(prefix(l-1),history)
            req=csum-k
            #check if req in seen prefixes so far
            if req in seen:
                subcnt+=seen[req]#add the number of times we seen that prefix
                #push the current prefix in hashmap
            seen[csum]=seen.get(csum,0)+1
        return subcnt        
        

        