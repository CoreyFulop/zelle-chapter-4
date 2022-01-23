# triangle_information.py

from re import A
from graphics import *
import math

def main():
    win = GraphWin("Triangle information", 500, 500)
    win.setCoords(0, 0, 100, 100)

    print("This program displays information about a traingle you draw.")
    print("Click three points on the window")

    # First point
    p1 = win.getMouse()

    x1 = p1.getX()
    y1 = p1.getY()

    # Draw the first point
    circle_1 = Circle(Point(x1, y1), 1)
    circle_1.draw(win)

    # Second point
    p2 = win.getMouse()

    x2 = p2.getX()
    y2 = p2.getY()

    # Draw the second point
    circle_2 = Circle(Point(x2, y2), 1)
    circle_2.draw(win)

    # Third point
    p3 = win.getMouse()

    x3 = p3.getX()
    y3 = p3.getY()

    circle_1.undraw()
    circle_2.undraw()

    # Draw triangle
    triangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    triangle.setFill("red")
    triangle.draw(win)

    # Get data on triangle
    dx1 = x2 - x1
    dy1 = y2 - y1
    a = math.sqrt(dx1**2 + dy1**2)

    dx2 = x3 - x2
    dy2 = y3 - y2
    b = math.sqrt(dx2**2 + dy2**2)

    dx3 = x3 - x1 
    dy3 = y3 - y1
    c = math.sqrt(dx3**2 + dy3**2)

    perimeter = a + b + c
    s = (perimeter)/2
    area = math.sqrt(s* (s - a) * (s - b) * (s - c))

    print(f"The perimeter of the triangle is {perimeter}.")
    print(f"The area of the triangle is {area}.")
    print("Click on the window to close.")

    win.getMouse()
    win.close()

main()