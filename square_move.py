# square_move.py

from graphics import *

def main():

    win = GraphWin()

    shape = Rectangle(Point(45,45), Point(55, 55))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        new = shape.clone()
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        new.move(dx, dy)
        new.draw(win)

    Text(Point(100,100), "Click again to quit").draw(win)

    win.getMouse()

    win.close()

main()