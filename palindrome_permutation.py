def is_pal_perm(s):
    s = s.lower()
    s = s.strip()
    
    letters = dict()
    num_odd = 0

    for c in s:
        if letters.get(c) == None:
            letters[c] = 1
        else:
            letters[c] += 1
    
    for num in letters.values():
        if num%2 == 1:
            num_odd += 1

    if len(s)%2 == 0:
        return num_odd == 0
    else:
        return num_odd <= 1

print(is_pal_perm('taco cat'))
