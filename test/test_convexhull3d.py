import unittest
from convexhull.convexhull3d import ConvexHull3D


class TestConvexHull3D(unittest.TestCase):
    def testCreateConvexHull_case1(self):
        test_data = [[0, 0, 0], [2, 0, 0], [0, 3, 0], [2, 3, 0], [1, 1, 5], [1, 1, -5], [1, 1, 0]]
        expected_output = [[4, 1, 0],
                           [2, 4, 0],
                           [1, 5, 0],
                           [5, 2, 0],
                           [4, 3, 1],
                           [3, 4, 2],
                           [3, 5, 1],
                           [5, 3, 2]]
        expected_output = [sorted(i) for i in expected_output]
        expected_output = sorted(expected_output, key=lambda x: tuple(x))
        output = ConvexHull3D(test_data).get_convexhull()
        output = [sorted(i) for i in output]
        output = sorted(output, key=lambda x: tuple(sorted(x)))
        self.assertEquals(expected_output, output)

    def testCreateConvexHull_case2(self):
        test_data = [[-0.0222149361131852, -0.366434993563625, 0.3270621312102882],
                     [-0.06676722137887703, -0.1566931052661437, 0.4589771055234383],
                     [0.02820502736438535, 0.04189077954915421, 0.05832764185809314],
                     [0.3126723396709863, 0.08400649026409401, -0.1029227018383543],
                     [0.1781470954214661, 0.1182274414396169, 0.04860343742054274],
                     [-0.1220315663349177, 0.01546165115708642, -0.1360330368727753],
                     [-0.3072535691850387, -0.01073880122111998, -0.4870359524963758],
                     [0.3867462923626847, 0.04492879989084675, 0.118335500935405],
                     [-0.1352406177997967, 0.01093378431250691, -0.2358910583293913],
                     [0.3789805913148268, -0.4732086509216658, -0.2177962499836425]]
        expected_output = [[0, 9, 6],
                            [1, 0, 6],
                            [9, 0, 7],
                            [0, 1, 7],
                            [9, 3, 6],
                            [3, 9, 7],
                            [1, 4, 7],
                            [4, 3, 7],
                            [3, 4, 6],
                            [5, 1, 6],
                            [4, 5, 6],
                            [2, 4, 1],
                            [5, 2, 1],
                            [2, 5, 4]]
        expected_output = [sorted(i) for i in expected_output]
        expected_output = sorted(expected_output, key=lambda x: tuple(x))
        output = ConvexHull3D(test_data).get_convexhull()
        output = [sorted(i) for i in output]
        output = sorted(output, key=lambda x: tuple(sorted(x)))
        self.assertEquals(expected_output, output)

    def testCreateConvexHull_case3(self):
        test_data = [[0, 0, 0], [2, 0, 0], [0, 3, 0], [2, 3, 0], [1, 1, 0], [1, 1, -0], [1, 1, 0]]
        output =  ConvexHull3D(test_data).get_convexhull()
        self.assertIsNone(output)

if __name__ == '__main__':
    unittest.main()
