class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        result = []
        for x in nums1:
            freq[x] = freq.get(x, 0) + 1
        for x in nums2:
            if x in freq and freq[x] > 0:
                result.append(x)
                freq[x] -= 1
        return result
        