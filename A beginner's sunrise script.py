from tkinter import *

win = Tk()
win.configure(bg='#000')

red = 0
blue = 0
green = 0

def fadeColour():
    global win
    global red
    global blue
    global green

    red += 2
    blue += 1
    green += 1

    if red > 254:
        red=255

    if blue > 254:
        blue=255

    if green > 254:
        green = 255

    if blue < 256:
        colour = '#{:02x}{:02x}{:02x}'.format(red, blue, green)
        win.configure(bg=colour)

        win.after(20, fadeColour)


win.after(20, fadeColour)
win.mainloop()
