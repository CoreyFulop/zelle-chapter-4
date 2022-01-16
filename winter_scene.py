# winter_scene.py

from graphics import *

win = GraphWin("Winter Scene")

win.setCoords(0, 0, 100, 100)

sky = Rectangle(Point(0,20), Point(100, 100))
sky.setFill("blue")
sky.setOutline("blue")
sky.draw(win)

snowman1 = Circle(Point(30,38), 20)
snowman1.setFill("white")
snowman1.draw(win)

snowman2 = Circle(Point(30,65), 10)
snowman2.setFill("white")
snowman2.draw(win)

eye1 = Circle(Point(25, 65), 2)
eye1.setFill("black")
eye1.draw(win)

eye2 = eye1.clone()
eye2.move(10, 0)
eye2.draw(win)

ground = Rectangle(Point(0,0), Point(100, 20))
ground.setFill("white")
ground.setOutline("white")
ground.draw(win)

trunk = Rectangle(Point(70, 15), Point(80,40))
trunk.setFill("brown")
trunk.draw(win)

branch1 = Polygon(Point(60, 30), Point(90, 30), Point(75, 45))
branch1.setFill("green")
branch1.draw(win)

branch2 = branch1.clone()
branch2.move(0, 10)
branch2.draw(win)

branch3 = branch2.clone()
branch3.move(0, 10)
branch3.draw(win)

branch4 = branch3.clone()
branch4.move(0, 10)
branch4.draw(win)

win.getMouse()

win.close()