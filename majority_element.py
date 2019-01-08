from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hist = Counter(nums)
        half = len(nums)/2
        majority_element = None
        
        for element in hist.keys():
            if hist[element] > half:
                majority_element = element
                break
                
        return majority_element
