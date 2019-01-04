class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        overlap_x1 = False
        overlap_y1 = False
        
        overlap_x2 = False
        overlap_y2 = False
        
        rec1_xs = [rec1[0], rec1[2]]
        rec1_ys = [rec1[1], rec1[3]]
        
        rec2_xs = [rec2[0], rec2[2]]
        rec2_ys = [rec2[1], rec2[3]]
        
        for x in rec1_xs:
            if (rec2_xs[0] < x and rec2_xs[1] > x) or (rec2_xs[0] > x and rec2_xs[1] < x):
                overlap_x1 = True
                break
                
        for y in rec1_ys:
            if (rec2_ys[0] < y and rec2_ys[1] > y) or (rec2_ys[0] > y and rec2_ys[1] < y):
                overlap_y1 = True
                break
                
        for x in rec2_xs:
            if (rec1_xs[0] < x and rec1_xs[1] > x) or (rec1_xs[0] > x and rec1_xs[1] < x):
                overlap_x2 = True
                break
                
        for y in rec2_ys:
            if (rec1_ys[0] < y and rec1_ys[1] > y) or (rec1_ys[0] > y and rec1_ys[1] < y):
                overlap_y2 = True
                break
                
        print(overlap_x1, 'overlap x1')
        print(overlap_y1, 'overlap y1')
        print(overlap_x2, 'overlap x2')
        print(overlap_y2, 'overlap y2')
                
        return (overlap_x1 and overlap_y1) or (overlap_x2 and overlap_y2) or (overlap_x1 and overlap_y2) or (overlap_x2 and overlap_y1)