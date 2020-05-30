'''
class rango(object):
    def __init__(self, i, f=0, p=1):
        self.i = i-1
        self.f = f
        self.p = p
        if(self.f == 0):
            self.i = f-1
            self.f = i
    def __iter__(self):
        return self
    def __next__(self):
        self.i += self.p
        if(self.i < self.f):
            return self.i
        else:
            raise StopIteration

for n in range(0,100, 20):
    print(n)
'''
from tkinter import *

tk = Tk()

tk.geometry("800x600")

tk.mainloop()