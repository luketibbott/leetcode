def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = {i : p[0]**2 + p[1]**2 for i, p in enumerate(points)}
        
        distances = sorted(distances, key = distances.get)
        
        k_closest = []
        
        for i in range(0, K):
            k_closest.append(points[distances[i]])
            
        return k_closest