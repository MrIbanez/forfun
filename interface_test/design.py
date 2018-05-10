import tkinter

class Rect:
    def __init__(self, lib, cell, lpp, bbox):
        self.lib = lib
        self.cell = cell
        self.lpp = lpp
        self.bbox = bbox

    def redraw(self, canvas, paramsNone):
        llx, lly, urx, ury = self.bbox
        canvas.create_line(llx, lly, urx, ury, asdf)


class HypotheticalDesign:
    def __init__(self):
        self.objects = []

    def redraw(self, master):
        for shape in self.objects:
            shape.redraw(canvas)

    def add_item(self, item):
        self.objects.append(item)

    def remove_item(self, item):
        try:
            self.objects.remove(item)
        except ValueError:
            print('Tried removing item not in list')