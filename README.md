# JingChi OA 2

## Question description

1. Given a set of 2D points, compute the convex hull. (Convex hull is the smallest convex polygon containing

the points).

2. Given some more points, find if they are inside the convex hull

3. Can you extend above problems to 3D points

## How to Run

1. clone this repo
2. Run the test cases use ` python -m unittest discover -v`
3. To run python script taking input from stdin use `cat test.txt | convexhull/convexhull2d.py`
## Input Format

First line of input will contain a integer, N, number of points. Point can be 2 dimension or 3 dimension.

Then follow N + K lines where each line contains the coordinate of points seperate by space. The K lines represent point we want to check if they are within the constructed convexhull. 

## Output Format
A sequence of 2D point which represent a polygon. Starting 

### Sample Input 2D
```
6
1 1
2 2
2 0
2 4
3 3
4 2
0 0
10 12
2 3
```

### Sample Output 2D
```
JINXUANs-MacBook-Pro:jingchi_oa2 jinxuanwu$ cat test.txt | convexhull/convexhull2d.py 
Construct 2D convexhull for a set of 6 points
Result convexhull is: 
[2, 0]
[4, 2]
[3, 3]
[2, 4]
[1, 1]
point 0, 0 is not within the convexhull
point 10, 12 is not within the convexhull
point 2, 3 is within the convexhull
```
### Sample Input 3D:
```
7
0 0 0
2 0 0 
0 3 0
2 3 0
1 1 5
1 1 -5
1 1 0

```
### Sample Output 3D
```
JINXUANs-MacBook-Pro:jingchi_oa2 jinxuanwu$ cat test_data_3d.txt | ./convexhull/convexhull3d.py 
Construct 3D convexhull for a set of 7 points
Result convexhull is: 
[0, 1, 4]
[2, 0, 4]
[3, 2, 4]
[1, 3, 4]
[1, 0, 5]
[3, 1, 5]
[2, 3, 5]
[0, 2, 5]

```
## Explantation
1. For 2D convex hull, I choose to use Graham Scan algorithm to calculate the convex hull of given point list. Complexity is O(nlogn)
2. For 3D convexhull I use incremental construction algorithm.  


 