import unittest
from convexhull.convexhull2d import ConvexHull2D


class TestConvexHull2D(unittest.TestCase):
    def testCreateConvexHull_case1(self):
        test_data = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
        expected_output = [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]
        self.assertEquals(sorted(expected_output), sorted(ConvexHull2D(test_data).get_convexhull()))

    def testCreateConvexHull_case2(self):
        test_data = [[1, 1], [2, 2], [2, 0], [1, 0], [2, 4], [3, 3], [4, 2]]
        expected_output = [[1, 1], [1, 0], [2, 0], [4, 2], [3, 3], [2, 4]]
        self.assertEquals(sorted(expected_output), sorted(ConvexHull2D(test_data).get_convexhull()))

    def testCreateConvexHull_case3(self):
        test_data = [[1, 1], [1, 2], [2, 0], [1, 0], [2, 4], [3, 3], [4, 2]]
        expected_output = [[1, 1], [1, 0], [2, 0], [4, 2], [3, 3], [2, 4]]
        self.assertEquals(sorted(expected_output), sorted(ConvexHull2D(test_data).get_convexhull()))

if __name__ == '__main__':
    unittest.main()
