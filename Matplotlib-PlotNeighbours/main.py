import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

'''steps : 
1. input the points --> list of tuple of points for plotting points
2. compute distance btw every pair of points --> the list of tuple of closest/neighbouring points (point's indices) for connecting lines 
3. scatter the the inputted points from points & plot/connect the neighbour point pairs acc to lines 
'''

#finding distance btween 2 points using euclidean formula 
def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

#getting points from user and unpack them to return a list of tuples of coordinates of point 
def getPoints():
    points = []
    n = int(input("Enter the number of points: "))
    for i in range(n):
        x, y = map(float, input(f"Enter x and y for point {i+1}: ").split())
        points.append((x, y))
    return points

#take points as parameter and form a set of tuples of neighbouring points (indices in  points)
def getLines(points):
    lines = set() #avoid duplicate connections
    for i, point in enumerate(points):
        distances = [(distance(point, points[j]), j) for j in range(len(points)) if j!=i] #list of tuples of index of each point and its distance from the fixed point of each iteration
        distances.sort() #sort by disatnce element of tuple 
        nearest = distances[0][1] #nearest neghbour point in points 
        line = tuple(sorted((i, nearest))) #to avoid duplicate connections (std)
        lines.add(line)
    return lines
            

def plot(points,lines):
    #scatter all the points
    x = [points[i][0] for i in range(len(points))] #unpacking x and y coordinates from points
    y = [points[i][1] for i in range(len(points))]
    plt.scatter(x, y, c='red', marker='o')
    #plot each connection (line)
    for i in range(len(lines)):
        #unpacking neighbouring pairs on each iteration then plotting
        x = [points[lines[i][0]][0], points[lines[i][1]][0]]
        y = [points[lines[i][0]][1], points[lines[i][1]][1]]
        plt.plot(x, y, 'r-')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Plot of Closest Neighbour Points')
    plt.show()


if __name__ == "__main__":
    points = getPoints()
    lines = list(getLines(points))
    plot(points, lines)


'''
TESTCASE 1 : <./testcase-1.png>

points = [(2.0, 3.0), (4.0, 5.0), (5.0, 0.0), (0.0, 9.0)] are the all points to be plotted

lines = [(0, 1), (0, 2), (1, 3)]
(2,3) <--> (4,5), (2,3) <--> (5,0), (4,5) <--> (0,9) are the closest neghbouring pairs need to be connected by lines 


'''