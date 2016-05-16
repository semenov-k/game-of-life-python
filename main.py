from tkinter import *
import Timetest

class App(Tk):
    # canvas size in pixels
    HEIGHT = 500
    WIDTH = 600
    CELL_SIZE = 5

    InGame = False

    def __init__(self):
        Tk.__init__(self)
        App.root = self
        self.title("Game of Life")
        self.resizable(width=False, height=False)
        # GUI
        top_frame = Frame(self)
        self.bStart = Button(top_frame, text="Start", width=10, command=self.bStart_handler)
        self.bStart.grid(row=0, column=0)
        self.bStop = Button(top_frame, text="Stop", width=10, state=DISABLED, command=self.bStop_handler)
        self.bStop.grid(row=0, column=1)
        Button(top_frame, text="Clear", width=10, command=self.bClear_handler).grid(row=0, column=3)
        speed_frame = Frame(self)
        App.fps_scale = Scale(speed_frame, orient=HORIZONTAL, length=300, from_=10, to=100, tickinterval=10, resolution=5, label="Delay", showvalue=0)
        App.fps_scale.set(50)
        App.fps_scale.grid()
        speed_frame.grid(row=0)
        top_frame.grid(pady=10, row=1)

        canvas = Canvas(self, height=App.HEIGHT, width=App.WIDTH)
        canvas.grid()

        self.field = App.Field(canvas)
        Button(top_frame, text="One step", width=10, command=self.field.calculation_of_life).grid(row=0, column=2)

        canvas.bind("<B1-Motion>", self.field.draw_start_state)
        canvas.bind("<ButtonPress-1>", self.field.draw_start_state)
        self.mainloop()
    #Buttons event handlers
    def bStart_handler(self):
        self.bStart["state"] = DISABLED
        self.bStop["state"] = ACTIVE
        App.InGame = True
        self.field.calculation_of_life()

    def bStop_handler(self):
        self.bStart["state"] = ACTIVE
        self.bStop["state"] = DISABLED
        App.InGame = False

    def bClear_handler(self):
        for y in range(len(self.field.matrix) - 1):
            for x in range(len(self.field.matrix[y]) - 1):
                self.field.matrix[y][x].set_dead()

    class Field:
        class Cell:
            def __init__(self, x, y, canvas):
                self.alive = False
                self.rect = canvas.create_rectangle(x, y, x + App.CELL_SIZE, y + App.CELL_SIZE, fill="black", outline="#013220")
                self.canvas = canvas
                self.next_gen = self.alive

            def set_alive(self):
                self.alive = True
                self.canvas.itemconfig(self.rect, fill="red")

            def set_dead(self):
                self.alive = False
                self.canvas.itemconfig(self.rect, fill="black")

        def __init__(self, canvas):
            self.matrix = []
            for y in range(int(App.HEIGHT / App.CELL_SIZE) - 1):
                temp = []
                for x in range(int(App.WIDTH / App.CELL_SIZE) - 1):
                    temp.append(self.Cell(x * App.CELL_SIZE + 5, y * App.CELL_SIZE + 5, canvas))
                self.matrix.append(temp)
        def next_generation(self):
            for y in range(len(self.matrix) - 1):
                for x in range(len(self.matrix[y]) - 1):
                    if self.matrix[y][x].next_gen:
                        self.matrix[y][x].set_alive()
                    else:
                        self.matrix[y][x].set_dead()

        def draw_start_state(self, event):
            if not App.InGame and 0 < event.x < App.WIDTH and 0 < event.y < App.HEIGHT:
                self.matrix[(event.y - 5) // App.CELL_SIZE][(event.x - 5) // App.CELL_SIZE].set_alive()

        def calculation_of_life(self):
            around_vector = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for y in range(len(self.matrix) - 1):
                for x in range(len(self.matrix[y]) - 1):
                    counter = 0
                    for vector in around_vector:
                        try:
                            if self.matrix[y + vector[0]][x + vector[1]].alive:
                                counter += 1
                        except IndexError:
                            pass
                    if self.matrix[y][x].alive:
                        if not (2 <= counter <= 3):
                            self.matrix[y][x].next_gen = False
                        else:
                            self.matrix[y][x].next_gen = True
                    else:
                        if counter == 3:
                            self.matrix[y][x].next_gen = True
            self.next_generation()
            if App.InGame:
                App.root.after(App.fps_scale.get(), self.calculation_of_life)
if __name__ == "__main__":
    app = App()




