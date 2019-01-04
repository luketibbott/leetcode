class solution:    
    def intToRoman(self, num):
            """
            :type num: int
            :rtype: str
            """
            int_to_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                            4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
            
            digits = []
            
            roman = ''
            
            while num != 0:
                digits.append(num%10)
                num = num // 10
                
            #digits = list(reversed(digits))
                
            for dig, magnitude in zip(digits, range(len(digits))):
                current_place = dig*10**magnitude
                if current_place in int_to_roman.keys():
                    roman = int_to_roman[current_place] + roman
                
                # Find nearest numeral that's less than dig*10**magnitude
                elif current_place != 0:
                    while current_place > 0:
                        nearest = 0
                        for key in int_to_roman.keys():
                            if (key <= current_place) and (key > nearest):
                                nearest = key
                                
                        if current_place > nearest:
                            roman += int_to_roman[nearest]
                        else:
                            roman = int_to_roman[nearest] + roman
                            
                        current_place -= nearest
                            
            return roman

sol = solution()

n = input()

print(sol.intToRoman(n))