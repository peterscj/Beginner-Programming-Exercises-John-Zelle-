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
    message = Text(Point(300, 600), 'Click anywhere to change the image to gray scale!')
    message.draw(win)
    win.getMouse()

    for i in range(height):
        for j in range(width):
            colors = pic.getPixel(i, j)
            r, g, b = int(colors[0]), int(colors[1]), int(colors[2])
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            new.setPixel(i, j, color_rgb(brightness, brightness, brightness))

    new.draw(win)

