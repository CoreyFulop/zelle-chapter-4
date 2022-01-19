# circle_intersection.py
# Computes the points of intersection of a horizontal line with
# a circle centered on (0,0).

from graphics import *

import math 

def main():
    
    # Get input
    r = eval(input("Enter the radius of the circle: "))
    y = eval(input("Enter the y-intercept of the horizontal line: "))

    # Determine x coordinates of intersection
    x_intersection_1 = math.sqrt(r**2 - y**2)
    x_intersection_2 = - math.sqrt(r**2 - y**2)

    # Graphically depict system
    
    win = GraphWin("Circle Intersection", 300, 300)
    win.setCoords(-10, -10, 10, 10)

    circle = Circle(Point(0,0), r)
    circle.setOutline("blue")
    circle.draw(win)

    line = Line(Point(-10, y), Point(10, y))
    line.draw(win)

    intersect_1 = Circle(Point(x_intersection_1, y), 0.2)
    intersect_1.setFill("red")
    intersect_1.draw(win)

    intersect_2 = Circle(Point(x_intersection_2, y), 0.2)
    intersect_2.setFill("red")
    intersect_2.draw(win)

    # Print results
    print(f"The x values of the points of intersection are {x_intersection_1} and {x_intersection_2}.")

    # Click on window to exit
    win.getMouse()
    win.close()

main()