# rectangle_information.py

from graphics import *

import math

def main():
    
    win = GraphWin("Rectangle information", 500, 500)
    win.setCoords(0, 0, 100, 100)

    print("Click two points on the window for opposite corners of a rectangle.")

    p1 = win.getMouse()
    p2 = win.getMouse()

    x1 = p1.getX()
    y1 = p1.getY()

    x2 = p2.getX()
    y2 = p2.getY()

    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    rectangle.setFill("red")
    rectangle.draw(win)

    length = math.sqrt((x1-x2)**2)
    width = math.sqrt((y1-y2)**2)

    area = length * width
    perimeter = 2 * (length + width)

    print(f"The area of the rectangle is {area}, and the perimeter is {perimeter}.")
    print("Click on the window to close.")

    win.getMouse()
    win.close()

main()