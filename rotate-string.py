def rotateString(A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == '' and B == '':
            return True
        elif A == '' or B == '':
            return False
        first_char = A[0]
        
        shift_candidates = [i for i in range(len(B)) if B[i] == first_char]
        
        for cand in shift_candidates:
            if A == B[cand:] + B[:cand]:
                return True
        
        return False