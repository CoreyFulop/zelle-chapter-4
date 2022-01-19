#graphical_future_value.py

from graphics import *

def main():

    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(0, 0, 100, 100)

    intro = Text(Point(50,80), "This program plots the growth of a 10-year investment")
    intro.draw(win)

    # Get inputs and wait for mouse click
    text1 = Text(Point(40, 50), "Principal:")
    text1.draw(win)

    input1 = Entry(Point(50,50), 5)
    input1.setText("0.0")
    input1.draw(win)

    text2 = Text(Point(43, 40), "apr:")
    text2.draw(win)

    input2 = Entry(Point(50,40), 5)
    input2.setText("0.0")
    input2.draw(win)

    text3 = Text(Point(50, 30), "Click anywhere to continue")
    text3.draw(win)

    win.getMouse()

    # Set input to correct type
    principal = eval(input1.getText())
    apr = eval(input2.getText())

    # Undraw input fields
    text1.undraw()
    text2.undraw()

    text3.undraw()

    input1.undraw()
    input2.undraw()

    # Create labels on left edge
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), " 0.0K").draw(win)
    Text(Point(-1, 2500), " 2.5K").draw(win)
    Text(Point(-1, 5000), " 5.0K").draw(win)
    Text(Point(-1, 7500), " 7.5K").draw(win)
    Text(Point(-1, 10000), "10.0K").draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    Text(Point(5, 10000), "Click anywhere to exit").draw(win)

    win.getMouse()

    win.close()

main()