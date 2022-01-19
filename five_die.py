# five_die.py

from graphics import *

win = GraphWin("A straight", 500, 500)
win.setCoords(0, 0, 100, 100)
win.setBackground("grey")

outline1 = Rectangle(Point(2.4, 42.5), Point(17.5, 57.5))
outline1.setFill("white")
outline1.draw(win)

dot1 = Circle(Point(10,50), 2)
dot1.setFill("black")
dot1.draw(win)

outline2 = outline1.clone()
outline2.move(20, 0)
outline2.draw(win)

dot2 = dot1.clone()
dot2.move(17, 0)
dot2.draw(win)

dot3 = dot1.clone()
dot3.move(23, 0)
dot3.draw(win)

outline3 = outline2.clone()
outline3.move(20, 0)
outline3.draw(win)

dot4 = dot1.clone()
dot4.move(40, 3)
dot4.draw(win)

dot5 = dot2.clone()
dot5.move(20, -3)
dot5.draw(win)

dot6 = dot3.clone()
dot6.move(20, -3)
dot6.draw(win)

outline4 = outline3.clone()
outline4.move(20, 0)
outline4.draw(win)

dot7 = dot5.clone()
dot7.move(20, 6)
dot7.draw(win)

dot8 = dot6.clone()
dot8.move(20, 6)
dot8.draw(win)

dot9 = dot5.clone()
dot9.move(20,0)
dot9.draw(win)

dot10 = dot6.clone()
dot10.move(20, 0)
dot10.draw(win)

outline5 = outline4.clone()
outline5.move(20, 0)
outline5.draw(win)

dot11 = dot7.clone()
dot11.move(20, 1)
dot11.draw(win)

dot12 = dot8.clone()
dot12.move(20, 1)
dot12.draw(win)

dot13 = dot1.clone()
dot13.move(80, 0)
dot13.draw(win)

dot14 = dot9.clone()
dot14.move(20, -1)
dot14.draw(win)

dot15 = dot10.clone()
dot15.move(20, -1)
dot15.draw(win)

win.getMouse()
win.close()