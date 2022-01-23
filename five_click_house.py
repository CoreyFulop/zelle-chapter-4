# five_click_house.py

from graphics import *
import math

def main():
    print("This program produces a house from five clicks in the window")

    win = GraphWin("Five click house", 500, 500)
    win.setCoords(0, 0, 100, 100)

    # Get points

    # Point 1
    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()

    circle_1 = Circle(Point(x1, y1), 1)
    circle_1.draw(win)

    # Point 2
    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()

    circle_2 = Circle(Point(x2, y2), 1)
    circle_2.draw(win)

    # Point 3
    p3 = win.getMouse()
    x3 = p3.getX()
    y3 = p3.getY()

    circle_3 = Circle(Point(x3, y3), 1)
    circle_3.draw(win)

    # Point 4
    p4 = win.getMouse()
    x4 = p4.getX()
    y4 = p4.getY()

    circle_4 = Circle(Point(x4, y4), 1)
    circle_4.draw(win)

    # Point 5
    p5 = win.getMouse()
    x5 = p5.getX()
    y5 = p5.getY()

    circle_5 = Circle(Point(x5, y5), 1)
    circle_5.draw(win)  


    circle_1.undraw()
    circle_2.undraw()
    circle_3.undraw()
    circle_4.undraw()
    circle_5.undraw()

    # Draw house

    # Draw frame
    frame = Rectangle(Point(x1, y1), Point(x2, y2))
    frame.draw(win)

    # Draw door
    dx = x2 - x1
    door_width = (1/5) * math.sqrt(dx**2)
    half_door_width = (1/2) * door_width
    door = Rectangle(Point(x3 - half_door_width, y3), Point(x3 + half_door_width, y1))
    door.draw(win)

    # Draw window
    window_width = (1/2) * door_width
    half_window_width = (1/2) * window_width
    window = Rectangle(Point(x4 - half_window_width, y4 + half_window_width), Point(x4 + half_window_width, y4 - half_window_width))
    window.draw(win)

    # Draw roof
    roof = Polygon(Point(x1, y2), Point(x2, y2), Point(x5, y5))
    roof.draw(win)


    print("Click the window to exit.")
    win.getMouse()
    win.close()    
    
main()