from tkinter import *
from random import randint


#  http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#  http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  http://zetcode.com/gui/tkinter/drawing/
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.toolsThickness = 2
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)

        self.pack()

        master.bind('a', self.thicknessPlus)
        master.bind('s', self.thicknessMinus)

    def setPreviousXY(self, event):
        print("now")
        self.previousX = event.x
        self.previousY = event.y

    def draw(self, event):
        # line 1
        if self.radiobuttonValue.get() == 1:
            self.myCanvas.create_oval(event.x - self.toolsThickness,
                                      event.y - self.toolsThickness,
                                      event.x + self.toolsThickness,
                                      event.y + self.toolsThickness,
                                      fill=self.rgb
                                      )
        # line 2
        elif self.radiobuttonValue.get() == 2:
            self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width=self.toolsThickness,
                                      fill=self.rgb)
            self.previousX = event.x
            self.previousY = event.y
            # flowers tool
        elif self.radiobuttonValue.get() == 3:
            tk_rgb = "#%02x%02x%02x" % (randint(140, 255), randint(140, 225), 40)
            self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width=self.toolsThickness,
                                      fill=tk_rgb)
        # spray tool
        elif self.radiobuttonValue.get() == 4:
            if self.toolsThickness < 5:
                multiplier = 6
            else:
                multiplier = 2
            xrand = randint(-self.toolsThickness * multiplier,
                            +self.toolsThickness * multiplier)
            yrand = randint(-self.toolsThickness * multiplier,
                            +self.toolsThickness * multiplier)

            self.myCanvas.create_oval(event.x + xrand, event.y + yrand,
                                      event.x + xrand + self.toolsThickness, event.y + yrand + self.toolsThickness,
                                      fill=self.rgb,
                                      width=0
                                      )
            # cosmos tool
        elif self.radiobuttonValue.get() == 5:
            if self.toolsThickness < 5:
                multiplier = 6
            else:
                multiplier = 2
            xrand = randint(-self.toolsThickness * multiplier,
                            +self.toolsThickness * multiplier)
            yrand = randint(-self.toolsThickness * multiplier,
                            +self.toolsThickness * multiplier)
            tk_rgb = "#%02x%02x%02x" % (randint(5, 255), randint(10, 150), randint(13, 255))
            self.myCanvas.create_oval(event.x + xrand, event.y + yrand,
                                      event.x + self.toolsThickness, event.y + self.toolsThickness,
                                      fill=tk_rgb
                                      )

    def delteAll(self):
        self.myCanvas.delete("all")

    def thicknessPlus(self, event):
        if self.toolsThickness < 25:
            self.toolsThickness += 1
            self.myScale.set(self.toolsThickness)

    def thicknessMinus(self, event):
        if 1 < self.toolsThickness:
            self.toolsThickness -= 1
            self.myScale.set(self.toolsThickness)


root = Tk()
root.title("Drawing program")
app = Application(root)
root.mainloop()
