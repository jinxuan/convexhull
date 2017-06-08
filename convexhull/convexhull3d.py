#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Provide the class to calculate convex hull of a list of 3 dimensional point.
Author: Jinxuan Wu
"""

from __future__ import division

import sys


class ConvexHull3D(object):
    def __init__(self, points=[]):
        self.points = points
        self.convexhull = []

    def vect(self, points, start, end):
        return [y - x for x, y in zip(points[start], points[end])]

    def cross(self, u, v):
        return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]

    def dot(self, u, v):
        return sum([x * y for x, y in zip(u, v)])

    def normal(self, points, face):
        u = self.vect(points, face[0], face[1])
        v = self.vect(points, face[0], face[-1])
        return self.cross(u, v)

    def seen(self, points, face, p):
        N = self.normal(points, face)
        P = self.vect(points, face[0], p)
        return (self.dot(N, P) >= 0)

    def bdry(self, faces):
        bdry_fw = set([(F[i - 1], F[i]) for F in faces for i in range(0, len(F))])
        bdry_bk = set([(F[i], F[i - 1]) for F in faces for i in range(0, len(F))])
        return bdry_fw - bdry_bk

    def addPoint(self, points, hull, p):
        """
        Add points to current hull, if the point is not in it. Update by  
        :param points: The input point list
        :param hull: Current ConvexHull in which we might need to add point and face to it
        :param p: Point that might need to add
        :return: None.
        """
        seenF = [F for F in hull if self.seen(points, F, p)]
        if len(seenF) == len(hull):  # if can see all faces, unsee ones looking "down"
            N = self.normal(points, seenF[0])
            seenF = [F for F in seenF if self.dot(self.normal(points, F), N) > 0]
        for F in seenF:
            hull.remove(F)
        for E in self.bdry(seenF):
            hull.append([E[0], E[1], p])

    def one_face(self, points, face, p):
        a, b, c = self.normal(points, face)
        d = -(a * points[face[0]][0] + b * points[face[0]][1] + c * points[face[0]][2])
        p_ = a * points[p][0] + b * points[p][1] + c * points[p][2]
        return p_ == d

    def get_convexhull(self):
        # make sure points are not on same line or same plane. Otherwise we couldn't find build the initial convex hull
        all_in_one_plane = True
        for i in range(3, len(self.points)):
            if not self.one_face(self.points, [0, 1, 2], i):
                all_in_one_plane = False
        if all_in_one_plane:
            return None
        else:
            hull = [[0, 1, 2], [0, 2, 1]]
            for i in range(3, len(self.points)):
                self.addPoint(self.points, hull, i)
            return hull


if __name__ == "__main__":
    if sys.stdin.isatty():
        print "Input a integer N, then follows N+K point sets"
        sys.exit()
    N = int(sys.stdin.readline())
    points_str_list = sys.stdin.readlines()
    all_points = map(lambda x: x.strip().split(), points_str_list)
    all_points = map(lambda x: [int(y) for y in x], all_points)
    convexhull_candidate_points = all_points[0:N]
    print "Construct 3D convexhull for a set of " + str(N) + " points"
    convexhull = ConvexHull3D(convexhull_candidate_points)
    print "Result convexhull is: "
    for point in convexhull.get_convexhull():
        print point
    for point in all_points[N:]:
        if convexhull.check_if_within_convexhull(point):
            print "point " + ", ".join([str(x) for x in point]) + " is within the convexhull"
        else:
            print "point " + ", ".join([str(x) for x in point]) + " is not within the convexhull"
