from tkinter import *

root = Tk()
root.title("Game Of Life")
#canvas size in pixels
HEIGHT = 500
WIDTH = 600
CELL_SIZE = 5

InGame = False

top_frame = Frame(root)
start_button = Button(top_frame, text="Start", width=10)
stop_button = Button(top_frame, text="Stop", width=10)
clear_button = Button(top_frame, text="Clear", width=10)
start_button.grid(row=0, column=0)
stop_button.grid(row=0, column=1)
clear_button.grid(row=0, column=2)
top_frame.grid()

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
canvas.grid()
class Cell:
    def __init__(self, x, y):
        self.alive = False
        self.rect = canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="white", outline="#dddddd")
    def change_state(self):
        if self.alive:
            self.alive = False
            self.rect["fill"] = "black"
        else:
            self.alive = True
            self.rect["fill"] = "white"
class Field:
    def __init__(self):
        self.matrix = []
        for y in range(int(HEIGHT/CELL_SIZE) - 1):
            temp = []
            for x in range(int(WIDTH/CELL_SIZE) - 1):
                temp.append(Cell(x * CELL_SIZE + 5, y * CELL_SIZE + 5))

field = Field()
root.mainloop()