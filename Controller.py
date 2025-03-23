import tkinter as tk
from PIL import ImageTk
from tkinter import filedialog, messagebox
from Timer import Timer


class ControlPanel:
    def __init__(self, board):
        self.photoPuzzle = ImageTk.PhotoImage(file='Images/puzzle.jpg')
        self.labelPuzzle = tk.Button(master=board, image=self.photoPuzzle, bg='gray', borderwidth=0)
        self.finished = True
        self.timer = None
        self.board = board

        def reset():
            self.finished = False
            self.state.place_forget()
            if self.timer is not None:
                self.timer.kill()
            board.puzzle.shuffle()
            self.timer = Timer(controller=self, n=board.n)
            self.timer.start()

        def load():
            path = tk.filedialog.askopenfilename(initialdir="/", title='Please select a directory')
            board.load(path=path, n=board.n)

        def level():
            def done():
                try:
                    n = int(nEnt.get())
                    if 1 < n < 10:
                        board.load(path=board.path, n=n)
                        root.destroy()
                    else:
                        messagebox.showerror('Enter size 2-9')
                except:
                    messagebox.showerror('Invalid input !')

            root = tk.Tk()
            nLabel = tk.Label(master=root, text='puzzle size : ')
            nLabel.grid(row=1, column=1, sticky="e")
            nEnt = tk.Entry(master=root, width=10)
            nEnt.grid(row=1, column=2, sticky="e")
            buttonDone = tk.Button(master=root, width=5, command=done, text='ok')
            buttonDone.grid(row=1, column=3, sticky="e")

        self.photoLoad = ImageTk.PhotoImage(file='Images/load.jpg')
        self.buttonLoad = tk.Button(master=board, command=load, image=self.photoLoad, bg='gray', borderwidth=0)

        self.photoReset = ImageTk.PhotoImage(file='Images/reset.jpg')
        self.buttonShuffle = tk.Button(master=board, command=reset, image=self.photoReset, bg='gray', borderwidth=0)

        self.photoLevel = ImageTk.PhotoImage(file='Images/level.jpg')
        self.buttonLevel = tk.Button(master=board, command=level, image=self.photoLevel, bg='gray', borderwidth=0)

        self.photoTime = ImageTk.PhotoImage(file='Images/time.jpg')
        self.labelTime = tk.Label(master=board, image=self.photoTime, bg='gray', borderwidth=0)

        self.labelPuzzle.place(x=615, y=40)
        self.buttonLoad.place(x=655, y=200)
        self.buttonShuffle.place(x=655, y=300)
        self.buttonLevel.place(x=655, y=400)
        self.labelTime.place(x=655, y=500)
        self.numbers = []
        for i in range(10):
            self.numbers.append(ImageTk.PhotoImage(file='Images/' + str(i) + '.jpg'))
        self.numbers.append(ImageTk.PhotoImage(file='Images/+.jpg'))

        self.t1 = tk.Label(master=self.labelTime, image=self.numbers[0], borderwidth=0)
        self.t2 = tk.Label(master=self.labelTime, image=self.numbers[0], borderwidth=0)
        self.t3 = tk.Label(master=self.labelTime, image=self.numbers[0], borderwidth=0)
        self.t4 = tk.Label(master=self.labelTime, image=self.numbers[0], borderwidth=0)
        self.t = tk.Label(master=self.labelTime, image=self.numbers[10], borderwidth=0)
        self.photoWin = ImageTk.PhotoImage(file='Images/win.jpg')
        self.photoLost = ImageTk.PhotoImage(file='Images/lost.jpg')
        self.state = tk.Label(master=board, borderwidth=0)

    def check(self):
        isWin = True
        k = 0
        for i in range(self.board.n):
            for j in range(self.board.n):
                if k < self.board.n * self.board.n - 1:
                    if self.board.puzzle.pieces[i][j].number != k:
                        isWin = False
                        break
                k += 1
        print(isWin)
        if isWin:
            self.win()

    def lost(self):
        self.finished = True
        self.state.place(x=655, y=500)
        self.state.configure(image=self.photoLost)

    def win(self):
        self.finished = True
        self.state.place(x=655, y=500)
        self.state.configure(image=self.photoWin)

    def reset(self):
        self.finished = True
        self.state.place_forget()
        if self.timer is not None:
            self.timer.T = 0
            self.timer.update()
