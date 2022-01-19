# line_segment_information.py

from graphics import *

import math

def main():

    win = GraphWin("Line information", 400, 400)
    win.setCoords(-100, -100, 100, 100)

    Line(Point(-100, 0), Point(100,0)).draw(win)
    Line(Point(0, -100), Point(0, 100)).draw(win)
    
    print("Click two points in the window to make a line segment.")
    
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Draw line segment
    segment = Line(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    segment.draw(win)

    mid_x = (p1.getX() + p2.getX())/2
    mid_y = (p1.getY() + p2.getY())/2

    # Depict midpoint
    center = Circle(Point(mid_x, mid_y), 2)
    center.setFill("cyan")
    center.draw(win)

    # Calculate line segment statistics
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = dy/dx
    length = math.sqrt(dx**2 + dy**2)

    print(f"The slope of the line is {slope} and the length is {length}.")
    print("Click on the window to close.")
    
    win.getMouse()
    win.close()

main()    