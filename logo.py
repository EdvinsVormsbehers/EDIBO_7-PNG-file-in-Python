from graphics import *


def main():
    win = GraphWin("My Window", 500, 500)
    # win.setBackground('blue')
    win.setBackground(color_rgb(255, 0, 50))

    pt = Point(250, 250)
    cir = Circle(pt, 100)
    cir.setFill(color_rgb(100, 50, 255))

    cir.draw(win)
    win.getMouse()
    win.close()


main()
