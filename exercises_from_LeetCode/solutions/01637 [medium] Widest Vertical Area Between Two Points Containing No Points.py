"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""

"""
Sortujemy dane punkty w zależnosci od x, przechodimy po posortowanej tablicy i liczymy roznice miedzy x,
najwieksza roznica jest naszym wynikiem 
"""
from math import inf

"todo gdzies zle sortuje"

class Solution:
    def partition(self, points, l, r):
        pivot = points[r][0]
        i = l - 1
        for j in range(l, r):
            if points[j][0] <= pivot:
                i += 1
                points[i], points[j] = points[j], points[i]
        points[i+1], points[r] = points[r], points[i+1]
        return i+1

    def quicksort(self, points, l, r):
        if l < r:
            q = self.partition(self, points, l, r)
            self.quicksort(self, points, l, q - 1)
            self.quicksort(self, points, q + 1, r)
        return points


    def maxWidthOfVerticalArea(self, points):
        self.quicksort(self, points, 0, len(points)-1)
        max_difference = -inf
        for i in range(len(points)-1):
            if points[i+1][0] - points[i][0] > max_difference:
                max_difference = points[i+1][0] - points[i][0]
        return max_difference


x = Solution
points = [[58,71],[64,41],[96,14],[26,37],[11,67],[84,2],[72,0],[16,95],[74,100],[60,98],[8,45],[6,59],[69,32],[93,12],
           [26,56],[9,39],[61,84],[54,93],[43,47],[84,40],[95,82],[17,85],[99,41],[96,24],[83,10],[82,62],[26,81],[74,96],
           [53,0],[11,72],[51,35],[33,3],[33,52],[58,94],[89,92],[54,85]]
print(x.maxWidthOfVerticalArea(x, points))
