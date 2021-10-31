class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
       if three points lie on the same line then the cross product of the vectors from the first point we chose (origin) will have a determinant of 0
        
        y2 - y1/x2 - x1
        
        """
        points.sort()
        numPoints = len(points)
        if numPoints == 1:
            return 1
        
        i, res = 0, 0
    
        while i < numPoints:
            
            j = i + 1
            while j < numPoints:
                temp = 1
                
                if points[j][0] == points[i][0]:
                    res = max(res, len([point for point in points if point[0] == points[j][0]]))
                    j+=1
                    continue
                
                grad = (points[j][1] - points[i][1])/(points[j][0] - points[i][0])
                k = j
                while k < numPoints:
                    if (points[k][1] - points[i][1])/(points[k][0] - points[i][0]) == grad:
                        temp += 1
                    k += 1
                res = max(res,temp)
                j += 1
            
            i += 1
        return res
