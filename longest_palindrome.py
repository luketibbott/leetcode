letter_freqs = dict()
        palindrome_length = 0
        used_one = False

        for char in s:
            if letter_freqs.get(char):
                letter_freqs[char] += 1
            else:
                letter_freqs[char] = 1
                
        for letter in letter_freqs.keys():
            
            letter_frequency = letter_freqs[letter]
            
            if letter_frequency == 1 and used_one == False:
                palindrome_length += 1
                used_one = True
                continue
            
            elif letter_frequency%2 == 0:
                palindrome_length += letter_frequency
                
            elif used_one == False:
                palindrome_length += letter_frequency
                used_one = True
                
            else:
                palindrome_length += letter_frequency - 1
                
                
        return palindrome_length
