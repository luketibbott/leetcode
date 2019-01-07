class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {5: 0, 10: 0, 20: 0}
        can_make = True
        
        for b in bills:
            if b == 5:
                change[5] += 1
                continue
                
            fives = change[5]
            tens = change[10]
            twenties = change[20]
            
            if fives == 0:
                can_make = False
                break
            
            # Already caught situations without fives in change, decrement fives
            if b == 10:
                change[5] -= 1
                    
            if b == 20:
                # Don't have three fives or one ten and one five
                if fives < 3 and (tens == 0 and fives < 3):
                    can_make = False
                    break
                
                # Give change using tens and fives if possible
                elif tens > 0 and fives > 0:
                    change[10] -= 1
                    change[5] -= 1
                    
                else:
                    change[5] -= 3
                    
            change[b] += 1                
        return can_make