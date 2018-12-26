# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

def compress_str(s):
    compressed_str = ''

    cur_char = s[0]
    cur_num = 1

    for i in range(1, len(s)):
        if s[i] == cur_char:
            cur_num += 1
        else:
            compressed_str += cur_char + str(cur_num)
            cur_char = s[i]
            cur_num = 1

    # Add final part of compressed string
    compressed_str += cur_char + str(cur_num)
            
    if len(compressed_str) > len(s):
        return s

    else:
        return compressed_str

s = 'sdddkdkkkkkkfkkkkkkuuurrrrppppqqqkkkdllllalllllslsssssssaaaaaaaammmmm'

print(compress_str(s))