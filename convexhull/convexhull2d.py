#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Provide the class to calculate convex hull of a list of 3 dimensional point.
Author: Jinxuan Wu
"""
from __future__ import division
import sys

class ConvexHull2D(object):
    def __init__(self, points=[]):
        self.points = points
        self.convexhull = []
    # Graham Scan
    def get_convexhull(self):
        num_points = len(self.points)
        if num_points <= 3: return self.points
        # point with lowest y then lowest x, this is begin of the convex hull;
        lb = min(self.points, key=lambda p: (p[1], p[0]))
        check_clock_wise = lambda p1, p2, p3: (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        distance_square = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        cmp = lambda p, q: check_clock_wise(lb, q, p) or distance_square(p, lb) - distance_square(q, lb)
        self.points.sort(cmp)
        cur = num_points - 1
        while cur and check_clock_wise(lb, self.points[cur], self.points[cur - 1]) == 0:
            cur -= 1
        points = self.points[:cur] + self.points[cur:][::-1]
        stack = [points[0], points[1]]
        for cur in range(2, num_points):
            while len(stack) > 1 and check_clock_wise(stack[-2], stack[-1], points[cur]) < 0:
                stack.pop()
            stack.append(points[cur])
        self.convexhull = stack
        return stack

    def check_if_within_convexhull(self, point):
        n = len(self.convexhull)
        inside = False
        x, y = point
        p1x, p1y = self.convexhull[0]
        for i in range(n + 1):
            p2x, p2y = self.convexhull[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

if __name__ == "__main__":
    if sys.stdin.isatty():
        print "Input a integer N, then follows N+K point sets"
        sys.exit()
    N = int(sys.stdin.readline())
    points_str_list = sys.stdin.readlines()
    all_points = map(lambda x:x.strip().split(), points_str_list)
    all_points = map(lambda x:[int(y) for y in x], all_points)
    convexhull_candidate_points = all_points[0:N]
    print "Construct 2D convexhull for a set of " + str(N) + " points"
    convexhull = ConvexHull2D(convexhull_candidate_points)
    print "Result convexhull for " + str(convexhull_candidate_points) + " is: "
    for point in convexhull.get_convexhull():
        print point
    for point in all_points[N:]:
        if convexhull.check_if_within_convexhull(point):
            print "point " + ", ".join([str(x) for x in point]) + " is within the convexhull"
        else:
            print "point " + ", ".join([str(x) for x in point]) + " is not within the convexhull"
