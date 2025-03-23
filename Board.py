from Reader import *
from Puzzle import *
from Controller import *
from PIL import ImageTk


class Board(tk.Tk):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.title('Sliding Puzzle')
        self.geometry('900x600')
        self.resizable(False, False)
        self.path = 'Images/bg.jpg'
        self.puzzle = None
        self.backgroundPhoto = ImageTk.PhotoImage(file=self.path)
        self.background = tk.Label(self, image=self.backgroundPhoto)
        self.background.place(x=0, y=0)
        self.controller = ControlPanel(self)
        self.load('Images/img.jpg', self.n)

    def load(self, path, n):
        if self.controller.timer is not None:
            self.controller.timer.kill()
        self.n = n
        self.path = path
        Reader(path=self.path, n=self.n)
        if self.puzzle is not None:
            self.puzzle.destroy()
        self.puzzle = Puzzle(master=self.background, n=self.n,board=self)
        self.puzzle.place(x=50, y=50)
        self.controller.reset()
        self.update()
