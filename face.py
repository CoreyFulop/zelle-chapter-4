# face.py

from graphics import *

win = GraphWin("Face")

win.setCoords(0, 0, 100, 100)

Center = Point(50, 50)

face = Circle(Center, 50)
face.setFill("yellow")
face.draw(win)

eye1 = Oval(Point(30,50), Point(40, 70))
eye1.setFill("black")
eye1.draw(win)

eye2 = eye1.clone()
eye2.move(30,0)
eye2.draw(win)

mouth = Line(Point(30, 25), Point(70, 25))
mouth.draw(win)

win.getMouse()

win.close()