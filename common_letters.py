from functools import reduce
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        
        c_list = list(map(Counter, A))
        
        letters = reduce(lambda x, y: x&y, c_list)
        
        for l in letters:
            for _ in range(letters[l]):
                result.append(l)
                
        return result