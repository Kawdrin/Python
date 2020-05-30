"""Calculadora RPG."""

from tkinter import *  # NOQA
from functools import partial

VERMELHO = '#913b36'


class Calculadora(object):
    """Top."""

    def __init__(self, tk): #NOQA
        self.font = ('Verdana', '20', 'bold')
        self.font2 = ('Verdana', '14', 'bold')

        logo = PhotoImage(file = 'bg_python.gif')

        #--------Frames--------
        # F que contem os checkbuttons
        self.frame1 = Frame(tk)
        self.frame1['bg'] = VERMELHO

        # F que contem os checkbuttons
        self.frame_c = Frame(tk)
        self.frame_c['bg'] = VERMELHO

        # F que contem a entrada de texto
        self.frame2 = Frame(tk)
        self.frame2[ 'bg'] = VERMELHO

        # F que contem o botao de calcular
        self.frame3 = Frame(tk)
        self.frame3['bg'] = VERMELHO

        self.frame_forget = Frame(tk)
        self.frame_forget['bg'] = VERMELHO

        # F que contem o texto das formulas
        self.frame4 = Frame(tk)
        self.frame4['bg'] = VERMELHO

        # F que contem os botões especificos
        self.frame5 = Frame(tk)
        self.frame5['bg'] = VERMELHO

        # Empacotando as Frames
        self.frame1.pack()
        self.frame_c.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame_forget.pack()
        self.frame4.pack()
        self.frame5.pack()
        #
        self.CriaElementos()

        # Titulo do apricativo
        self.img = Label(self.frame1)
        self.img['image'] = logo
        self.img.image = logo
        self.img.pack()

        self.bino_selecionado = False
        self.b_binominal = Checkbutton(self.frame_c, text = 'Modo Binominal', bg = VERMELHO, font = self.font, command = self.AtvBinominal)
        self.b_binominal.pack()

        #
        self.formula = Entry(self.frame2)
        self.formula.pack()
        #
        self.Calc = Button(self.frame3, text = 'Calcule',bg ='#d22d2d' , command = self.Calcular, font = self.font)
        self.Calc.pack()
        #

        self.resultado = Label(self.frame4, text='Resultado', fg = 'Blue', font = self.font)
        self.resultado.pack()

        self.botoes = ('-Habilidades-', "Atk's", 'Magias', 'HP', 'MANA', 'Scrols',
                       'DPS', 'Defesa', 'Monstros', 'Armas', 'Armaduras')

        for x, b in enumerate(self.botoes):
            if(x % 3 == 0):
                subframe = Frame(self.frame5)
                subframe.pack()
            self.bt = Button(subframe ,text = b ,bg = 'Green' ,width = 10 ,font = self.font2 ,command = partial(self.ColocaTexto, b))
            self.bt.pack(side = LEFT)

        self.b_Mapa = Button(subframe, text = 'Mapa', bg = 'Green', width = 10,font = self.font2)
        self.b_Mapa.pack(side = LEFT)

    def CriaElementos(self):
        self.l1 = Label(self.frame_forget, text = 'n = ')
        self.e1 = Entry(self.frame_forget)
        self.l2 = Label(self.frame_forget, text = 'P = ')
        self.e2 = Entry(self.frame_forget)

    def MostraElementos(self):
        self.l1.pack(side = LEFT)
        self.e1.pack(side = LEFT)
        self.l2.pack(side = LEFT)
        self.e2.pack(side = LEFT)

    def SomeElementos(self):
        self.l1.pack_forget()
        self.e1.pack_forget()
        self.l2.pack_forget()
        self.e2.pack_forget()

    def DestroiElementos(self):
        self.l1.destroy()
        self.e1.destroy()
        self.l2.destroy()
        self.e2.destroy()



    def ColocaTexto(self, texto):
        self.formula.insert(END, texto)

    def Msg(self, texto, cor = 'Red'):
        self.resultado['text'] = texto
        self.resultado['fg'] = cor

    def Calcular(self):
        self.Msg(self.formula.get(), 'Green')
        self.formula.delete(0, END)

    def AtvBinominal(self):
        self.bino_selecionado = not self.bino_selecionado
        if self.bino_selecionado:
            self.MostraElementos()
            self.Msg('Binominal Ativado')
        else:
            self.SomeElementos()
            self.Msg('Binominal Desativado', 'Green')

instancia = Tk()

Calculadora(instancia)

instancia.title('Calculadora')
instancia.geometry('600x550')

instancia['bg'] = '#913b36'

instancia.mainloop()
