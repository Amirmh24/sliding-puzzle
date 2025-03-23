from Piece import *
import random
import time


class Puzzle(tk.Label):
    def __init__(self, n, board, **kw):
        super().__init__(borderwidth=1, bg='gray', **kw)
        self.n = n
        self.board=board
        self.pieces = [[0 for i in range(self.n)] for j in range(self.n)]
        self.loc = (self.n - 1, self.n - 1)
        for i in range(self.n ** 2):
            piece = Piece(number=i, master=self, n=self.n, board=board)
            self.pieces[piece.r][piece.c] = piece
            self.pieces[piece.r][piece.c].grid(row=piece.r, column=piece.c)
        self.pieces[self.loc[0]][self.loc[1]].setNull()

    def setPiece(self, i, j, piece):
        self.pieces[i][j].number=piece.number
        self.pieces[i][j].setImage(piece.photo)

    def getPiece(self, i, j):
        return self.pieces[i][j]

    def moveD(self):
        if self.loc[0] > 0:
            i, j = self.loc[0], self.loc[1]
            self.setPiece(i, j, self.getPiece(i - 1, j))
            self.pieces[i - 1][j].setNull()
            self.loc = (i - 1, j)

    def moveU(self):
        if self.loc[0] < self.n - 1:
            i, j = self.loc[0], self.loc[1]
            self.setPiece(i, j, self.getPiece(i + 1, j))
            self.pieces[i + 1][j].setNull()
            self.loc = (i + 1, j)

    def moveR(self):
        if self.loc[1] > 0:
            i, j = self.loc[0], self.loc[1]
            self.setPiece(i, j, self.getPiece(i, j - 1))
            self.pieces[i][j - 1].setNull()
            self.loc = (i, j - 1)

    def moveL(self):
        if self.loc[1] < self.n - 1:
            i, j = self.loc[0], self.loc[1]
            self.setPiece(i, j, self.getPiece(i, j + 1))
            self.pieces[i][j + 1].setNull()
            self.loc = (i, j + 1)

    def shuffle(self):
        delay = 0.3
        for i in range(self.n * 300):
            a = random.randint(0, 3)
            if a == 0:
                self.moveD()
            elif a == 1:
                self.moveU()
            elif a == 2:
                self.moveR()
            elif a == 3:
                self.moveL()
            self.update()
            time.sleep(delay)
            if delay > 0.0001:
                delay = delay * 0.9
            else:
                delay = 0

