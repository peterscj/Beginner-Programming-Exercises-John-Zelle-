'''
Chapter 8 Exercise 15

Write a program to convert an image to its color negative. The general
form of the program will be similar to that of the previous problem. The
negative of a pixel is formed by subtracting each color value from 255. So
the new pixel color is color_rgb(255-r, 255-g, 255-b).

'''

from graphics import *

def main():

    win = GraphWin('test window', 500, 500)
    win.setCoords(0, 0, 650, 650)
    win.setBackground("white")

    # You will need to update this line of code with your own file.
    file = 'C:/Users/Cole/Documents/Read files/IRON_MAIDEN.ppm'



    pic = Image(Point(300, 300), file)
    width = pic.getWidth()
    height = pic.getHeight()
    # The Image object accepts width and height parameters, in addition to
    new = Image(Point(300, 100), width, height)

    pic.draw(win)
    message = Text(Point(300, 600), 'Click anywhere to change the image to color negative!')
    message.draw(win)
    win.getMouse()

    for i in range(height):
        for j in range(width):
            colors = pic.getPixel(i, j)
            r, g, b = int(colors[0]), int(colors[1]), int(colors[2])
            r_neg, g_neg, b_neg = 255-r, 255-g, 255-b
            new.setPixel(i, j, color_rgb(r_neg, g_neg, b_neg))

    new.draw(win)


