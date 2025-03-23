import threading
import time


class Timer(threading.Thread):
    def __init__(self, controller,n):
        super().__init__()
        self.controller = controller
        self.T = 60 * n * n
        self.isKilled = False
        self.update()

    def run(self):
        self.controller.t1.place(x=22, y=20)
        self.controller.t2.place(x=52, y=20)
        self.controller.t.place(x=82, y=20)
        self.controller.t3.place(x=97, y=20)
        self.controller.t4.place(x=127, y=20)
        while self.T > 0:
            if self.isKilled:
                break
            self.T -= 1
            time.sleep(1)
            try:
                self.update()
            except:
                print('stopped')
                break

        if not self.T > 0 and not self.isKilled:
            self.controller.lost()
            print('end')

    def update(self):
        min = self.T // 60
        sec = self.T % 60
        if len(str(min)) == 1:
            self.controller.t1.configure(image=self.controller.numbers[0])
            self.controller.t2.configure(image=self.controller.numbers[min])
        elif len(str(min)) == 2:
            self.controller.t1.configure(image=self.controller.numbers[min // 10])
            self.controller.t2.configure(image=self.controller.numbers[min % 10])

        if len(str(sec)) == 1:
            self.controller.t3.configure(image=self.controller.numbers[0])
            self.controller.t4.configure(image=self.controller.numbers[sec])
        elif len(str(sec)) == 2:
            self.controller.t3.configure(image=self.controller.numbers[sec // 10])
            self.controller.t4.configure(image=self.controller.numbers[sec % 10])

    def kill(self):
        self.isKilled = True
