import tkinter as tk
from PIL import ImageTk, Image


class Piece(tk.Button):
    def __init__(self, number, n, board, **kw):
        self.number = number
        self.n = n
        self.r = number // self.n
        self.c = number % self.n

        image = Image.open('crops/' + str(self.r) + '-' + str(self.c) + '.jpg')
        self.photo = ImageTk.PhotoImage(image)
        image = Image.open('crops/null.jpg')
        self.null = ImageTk.PhotoImage(image)

        def move():
            if not board.controller.finished:
                if self.r < board.puzzle.loc[0] and self.c == board.puzzle.loc[1]:
                    for i in range(board.puzzle.loc[0] - self.r):
                        board.puzzle.moveD()
                if self.r > board.puzzle.loc[0] and self.c == board.puzzle.loc[1]:
                    for i in range(self.r - board.puzzle.loc[0]):
                        board.puzzle.moveU()
                if self.r == board.puzzle.loc[0] and self.c < board.puzzle.loc[1]:
                    for i in range(board.puzzle.loc[1] - self.c):
                        board.puzzle.moveR()
                if self.r == board.puzzle.loc[0] and self.c > board.puzzle.loc[1]:
                    for i in range(self.c - board.puzzle.loc[1]):
                        board.puzzle.moveL()
                board.controller.check()

        super().__init__(image=self.photo, borderwidth=0, bg='black', command=move, **kw)

    def setNull(self):
        self.photo = self.null
        self.number = self.n * self.n - 1
        self.configure(image=self.photo)

    def setImage(self, photo):
        self.photo = photo
        self.configure(image=self.photo)
