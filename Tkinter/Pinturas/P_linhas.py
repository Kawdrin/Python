from tkinter import *
from conts import *

class PintarLinhas(object):
    def __init__(self, tk):

        tk.geometry(f'{ALTURA}x{LARGURA}')
        self.f_canvas = Frame(tk, bg = 'Grey')
        self.f_canvas.pack()

        self.f_botoes = Frame(tk, bg = AZUL)
        self.f_botoes.pack()

        self.canvas = Canvas(self.f_canvas, width = CANVAS_LAR, height = CANVAS_LAR, bg = 'White')
        self.canvas.pack()

        self.canvas.create_line(LARGURA/2, ALTURA/2, LARGURA/2, ALTURA/2)
        self.xy_p = [LARGURA/2, ALTURA/2]
        self.xy_s = [LARGURA/2, ALTURA/2]

        self.esquerda = Button(self.f_botoes, text = 'Esquerda', fg = 'Blue', command = self.Esquerda)
        self.esquerda.pack(side = LEFT)

        self.cima = Button(self.f_botoes, text = 'Cima', fg = 'Blue', command = self.Cima)
        self.cima.pack(side = LEFT)

        self.baixo = Button(self.f_botoes, text = 'Baixo', fg = 'Blue', command = self.Baixo)
        self.baixo.pack(side = LEFT)

        self.direita = Button(self.f_botoes, text = 'Direita', fg = 'Blue', command = self.Direita)
        self.direita.pack(side = LEFT)

    def Direita(self):
        self.xy_s[0] += 20
        self.canvas.create_line(self.xy_p, self.xy_s, fill = 'Purple')
        self.xy_p = self.xy_s[:]

    def Cima(self):
        self.xy_p[1] -= 20
        self.canvas.create_line(self.xy_p, self.xy_s, fill = 'Blue')
        self.xy_s = self.xy_p[:]

    def Baixo(self):
        self.xy_s[1] += 20
        self.canvas.create_line(self.xy_p, self.xy_s, fill = 'Green')
        self.xy_p = self.xy_s[:]

    def Esquerda(self):
        self.xy_p[0] -= 20
        self.canvas.create_line(self.xy_p, self.xy_s, fill = 'Red')
        self.xy_s = self.xy_p[:]

class PintarPolygon(object):
    def __init__(self, tk):
        tk.geometry('220x200')
        self.frame = Frame(tk, bg = 'Cyan')
        self.frame.pack()

        self.canvas = Canvas(self.frame, width = 500, height = 500, bg = 'Cyan')
        self.canvas.pack()

        self.canvas.create_polygon((20, 5), (200, 5), (200, 50), (110, 170), (20, 50), fill = 'White')
        self.canvas.create_polygon((28, 54), (107, 54), (107, 155), fill = 'Red')
        self.canvas.create_polygon((114, 54), (192, 54), (114, 155), fill = 'Black')

        self.canvas.create_rectangle((24, 9), (196, 43), fill = 'Black')
        self.canvas.create_text(110, 27, text = 'SPFC', fill = 'White', font = ('Verdana', 32, 'bold'))

class PintarCarinha(object):
    def __init__(self, tk):
        tk.geometry('400x400')
        tk.title('Carinha :D')

        self.frame_canvas = Frame(tk, bg = 'Cyan')
        self.frame_canvas.pack()

        self.canvas = Canvas(self.frame_canvas, width = 400, height = 400, bg = 'Cyan')
        self.canvas.pack()

        self.cara_x = self.cara_y = 200
        self.canvas.create_oval(self.cara_x, self.cara_y, self.cara_x + 30, self.cara_y + 30, fill = 'Yellow', outline = 'Black', tag = 'Cara')
        self.canvas.focus_force()
        self.canvas.bind('<Up>', self.Up)
        self.canvas.bind('<Down>', self.Down)
        self.canvas.bind('<Left>', self.Left)
        self.canvas.bind('<Right>', self.Right)

    def Up(self, event):
        if self.cara_y > 0:
            self.canvas.move('Cara', 0, -10)
            self.cara_y -= 10

    def Down(self, event):
        if self.cara_y < 400 - 30:
            self.canvas.move('Cara', 0, 10)
            self.cara_y += 10

    def Left(self, event):
        if self.cara_x > 0:
            self.canvas.move('Cara', -10, 0)
            self.cara_x -= 10

    def Right(self, event):
        if self.cara_x < 400 - 30:
            self.canvas.move('Cara', 10, 0)
            self.cara_x += 10

class PintarMario(object):
    def __init__(self, tk):
        tk.geometry('400x420')
        tk.resizable(False, False)
        tk.title('Mario')

        self.frame_canvas = Frame(tk, bg = 'Grey')
        self.frame_canvas.pack()

        self.canvas = Canvas(self.frame_canvas, width = 400, height = 400, bg = 'Black')
        self.canvas.pack()

        self.b_start = Button(tk, text = 'START', command = self.Comecar)
        self.b_start.pack()

        self.CriarSprites()

    def Comecar(self):
        self.image = PhotoImage(file = 'images/mario/mario_1.ppm')
        self.mario = self.canvas.create_image(200, 200, image = self.image, tag = 'Mario')
        self.canvas.focus_force()
        self.canvas.bind('<Left>', self.Left)
        self.canvas.bind('<Right>', self.Right)
        self.l = 0
        self.r = 0

    def Left(self, event):
        self.r = 0
        self.l += 1
        if self.l > 3:
            self.l = 0
        self.canvas.move('Mario', -10, 0)
        self.canvas.itemconfig(self.mario, image = self.spr_mario_left[self.l])

    def Right(self, event):
        self.l = 0
        self.r += 1
        if self.r > 3:
            self.r = 0
        self.canvas.move('Mario', 10, 0)
        self.canvas.itemconfig(self.mario, image = self.spr_mario_right[self.r])



    def CriarSprites(self):
        self.spr_mario_left = []
        self.spr_mario_right = []
        for sprite in range(1, 5):
            self.spr_mario_left.append(PhotoImage(file = f'images/mario/mario_l{sprite}.ppm'))
            self.spr_mario_right.append(PhotoImage(file = f'images/mario/mario_{sprite}.ppm'))
