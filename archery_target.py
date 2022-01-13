# archery_target.py

from graphics import *

win = GraphWin("Archery Target", 1000, 1000)

win.setCoords(0, 0, 100, 100)

win.setBackground("grey")

Center = Point(50, 50)

w = Circle(Center, 50)
w.setFill("white")
w.draw(win)

b = Circle(Center, 40)
b.setFill("black")
b.draw(win)

bl = Circle(Center, 30)
bl.setFill("blue")
bl.draw(win)

r = Circle(Center, 20)
r.setFill("red")
r.draw(win)

y = Circle(Center, 10)
y.setFill("yellow")
y.draw(win)

win.getMouse()

win.close()