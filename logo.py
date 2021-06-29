from graphics import *


def main():
    win = GraphWin("My Window", 500, 500)
    # win.setBackground('blue')
    win.setBackground(color_rgb(55, 0, 150))

    cir = Circle(Point(250, 250), 100)
    cir.setFill(color_rgb(255, 255, 255))
    cir.setWidth(5)
    cir.setOutline("red")

    cir2 = Circle(Point(250, 250), 110)
    cir2.setFill(color_rgb(255, 255, 255))
    cir2.setWidth(5)
    cir2.setOutline("red")

    cir3 = Circle(Point(250, 250), 120)
    cir3.setFill(color_rgb(255, 255, 255))
    cir3.setWidth(5)
    cir3.setOutline("red")

    lin1 = Line(Point(160, 200), Point(220, 350))
    lin1.setWidth(10)
    lin2 = Line(Point(220, 350), Point(250, 200))
    lin2.setWidth(10)
    lin3 = Line(Point(250, 200), Point(280, 350))
    lin3.setWidth(10)
    lin4 = Line(Point(280, 350), Point(340, 200))
    lin4.setWidth(10)

    cir3.draw(win)
    cir2.draw(win)
    cir.draw(win)
    lin1.draw(win)
    lin2.draw(win)
    lin3.draw(win)
    lin4.draw(win)

    win.getMouse()
    win.close()


main()
