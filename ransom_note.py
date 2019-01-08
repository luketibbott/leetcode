class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_chars = dict()
        constructable = True
        
        
        for char in magazine:
            if not magazine_chars.get(char):
                magazine_chars[char] = 1
            else:
                magazine_chars[char] += 1
                
        for char in ransomNote:
            if (not magazine_chars.get(char)) or magazine_chars[char] < 1:
                constructable = False
                break
                
            else:
                magazine_chars[char] -= 1
                
        return constructable
