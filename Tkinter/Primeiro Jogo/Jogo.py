from tkinter import *

tk = Tk()
tk.geometry('300x300')
tk.title('Grid Meu Lindo!')

titulo = Label(tk, text = 'Login')
titulo.grid(row = 0, column = 1, columnspan = 2, sticky = N, padx = 5, pady = 5)

l_login = Label(tk, text = 'Usúario:')
l_senha = Label(tk, text = 'Senha:')
l_login.grid(row = 1, column = 1)
l_senha.grid(row = 2, column = 1)

e_login = Entry(tk)
e_senha = Entry(tk, show = '*')
e_login.grid(row = 1, column = 2)
e_senha.grid(row = 2, column = 2)

tk.mainloop()


'''from random import choice
from const import *

class Jogo(object):
    """Organização de elementos."""
    def __init__(self):
        # Criação da Janela
        self.tk = Tk()
        self.tk.geometry(f'{CANVAS_LAR}x{LARGURA}')
        self.tk.resizable(False, False)
        self.tk.title('Block Brick')

        # Criação da Frame do Canvas
        self.frame = Frame(bg = 'Black')
        self.frame.pack()

        # Criação do Canvas
        self.canvas = Canvas(self.frame, bg = 'Black', width = CANVAS_LAR, height = CANVAS_ALT, cursor = 'cross')
        self.canvas.pack()

        self.start = Button(self.tk, text = 'Start', command = self.Comecar)
        self.start.focus_force()
        self.start.pack()

        self.start.bind('<Return>', self.Comecar)

        self.CarregarImagens()
        self.NovoJogo()

        self.tk.mainloop()
    def CarregarImagens(self):
        self.spritesheet = []
        for l in range(1, 91):
            self.spritesheet.append(PhotoImage(file = f'psico_bg/psico_{l:02}.gif'))

        self.sprites = 0
        self.limite = 91

    def NovoJogo(self):
        """Criar o player(retangulo) e os blocos aleatorios."""
        self.player_x = CANVAS_ALT//2
        self.player_vx = CANVAS_ALT//2
        self.player = self.canvas.create_rectangle((CANVAS_ALT//2, 440),(CANVAS_ALT//2 + 100, 425), fill = 'Blue', tag = 'Player')

        self.blocos = []
        l, c, e = 9, 10, 2 #Linhas, Colunas e Espaçamento
        xb, yb= 50, 20 #Base x, Base y, Posição inicial
        for li in range(l):
            self.cor = choice(['Orange', 'Blue', 'Green', 'Purple', 'Yellow', 'Red'])
            for co in range(c):
                self.bloco = self.canvas.create_rectangle((xb*(co+1)+2, yb*(li+1)+2), (xb*co+6, yb*(li+2)), fill = self.cor, outline = "White")
                self.blocos.append(self.bloco)

        self.b_x, self.b_y = (100, 200)
        self.b_vx = self.b_vy = 5
        self.canvas.create_oval(self.b_x, self.b_y, self.b_x + 30, self.b_y + 30, outline = 'White', fill = 'Red', tag = 'Bola')
        #self.canvas.create_text(CANVAS_LAR/2, CANVAS_ALT/2, text = 'Bom Jogo!', fill = 'Red', font = ('Fipps', 18))
        self.canvas.bind('<Motion>', self.MovimentarPlayer)
        self.jogando = True

    def Comecar(self,*event):
        self.Jogar()

    def Jogar(self):
        if(self.jogando):
            #self.Desenhar()
            self.Update()

            self.tk.after(10, self.Jogar)

    def Desenhar(self):
        self.sprites += 1
        if self.sprites == self.limite:
            self.sprites = 0
        self.canvas.create_image(CANVAS_LAR//2, CANVAS_ALT//2, image = self.spritesheet[self.sprites - 1])

    def Update(self):

        self.canvas.move('Bola', self.b_vx, self.b_vy)
        self.b_x += self.b_vx
        self.b_y += self.b_vy

        if(self.b_x > CANVAS_LAR - 30 or self.b_x < 0):
            self.b_vx *= -1

        if(self.b_y > CANVAS_ALT - 30 or self.b_y < 0):
            self.b_vy *= -1

        self.VerificaColisao()

    def MovimentarPlayer(self, event):
        if event.x > 0 and event.x  < CANVAS_ALT - 38:
            self.canvas.move('Player',(event.x - self.player_vx), 0)
            self.player_vx = event.x

        #self.player = self.canvas.create_rectangle((event.x, 440),(event.x + 100, 425), fill = 'Blue', tag = 'Player')

    def VerificaColisao(self):
        coord = self.canvas.bbox('Bola')

        colisoes = self.canvas.find_overlapping(*coord)
        if len(colisoes) != 0:
            if colisoes[0] != self.player:

                mais_proximo = self.canvas.find_closest(coord[0], coord[1])

                for bloco in self.blocos:
                    if bloco == mais_proximo[0]:
                        self.blocos.remove(bloco)
                        self.canvas.delete(bloco)

                        self.b_vy *= -1
            else:
                self.b_vy *= -1


if(__name__ == '__main__'):
    Jogo()
'''
