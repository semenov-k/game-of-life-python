from tkinter import *

root = Tk()
root.title("Game Of Life")
root.resizable(width=False, height=False)
#canvas size in pixels
HEIGHT = 500
WIDTH = 600
CELL_SIZE = 5

InGame = False

#GUI
top_frame = Frame(root)
start_button = Button(top_frame, text="Start", width=10)
stop_button = Button(top_frame, text="Stop", width=10, state=DISABLED)
clear_button = Button(top_frame, text="Clear", width=10)
start_button.grid(row=0, column=0)
stop_button.grid(row=0, column=1)
clear_button.grid(row=0, column=2)
top_frame.grid(pady=10)

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
canvas.grid()

class Field:
    class Cell:
        def __init__(self, x, y):
            self.alive = False
            self.rect = canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="white", outline="#dddddd")

        def set_alive(self):
            self.alive = True
            canvas.itemconfig(self.rect, fill="black")

        def set_dead(self):
            self.alive = False
            canvas.itemconfig(self.rect, fill="white")
    def __init__(self):
        self.matrix = []
        for y in range(int(HEIGHT/CELL_SIZE) - 1):
            temp = []
            for x in range(int(WIDTH/CELL_SIZE) - 1):
                temp.append(self.Cell(x * CELL_SIZE + 5, y * CELL_SIZE + 5))
            self.matrix.append(temp)
    def draw_start_state(self, event):
        if not InGame:
            self.matrix[(event.y - 5)//CELL_SIZE][(event.x - 5)//CELL_SIZE].set_alive()
    def calculation_of_life(self):
        around_vector = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for y in range(len(self.matrix) - 1):
            for x in range(len(self.matrix) - 1):
                counter = 0
                for vector in around_vector:
                    if self.matrix[x+vector[0]][y+vector[1]]:
                        counter += 1
                if self.matrix[x][y].alive:
                    if counter < 2:
                        self.matrix[x][y].set_dead()
                    if counter > 3:
                        self.matrix[x][y].set_dead()
                else:
                    if counter == 3:
                        self.matrix[x][y].set_alive()

field = Field()
canvas.bind("<B1-Motion>", field.draw_start_state)
canvas.bind("<ButtonPress-1>", field.draw_start_state)
root.mainloop()