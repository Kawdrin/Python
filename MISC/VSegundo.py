'''
if True:
    from tkinter import *

    tk = Tk()

    tk.geometry("800x600")
    tk.title("Ol'a, Mundo!")

    tk.mainloop()
'''
'''
if True:
    from tkinter import *

    tk = Tk()
    tk.title('Ola, Mundo!')

    texto = Label(tk, text = 'Ola Mundo!!', bg = 'Red', fg = 'Blue')
    texto.pack()

    tk.mainloop()
'''
'''
if True:
    from tkinter import *
        
    tk = Tk()

    tk.title('Brincando')
    tk.geometry('500x500')

    texto = Label(tk, text='Meu Mundo Loko')
    texto.pack()

    ent = Entry(tk)
    ent.pack()

    b = Button(tk, text='CLique',)
    b.pack()

    tk.mainloop()
'''
'''
if True:
    from tkinter import *

    tk = Tk()

    tk.title('Calculadora')
    tk.geometry('250x250')

    formula = Entry(tk)
    formula.pack()

    Calc = Button(tk, text = 'Cacule')
    Calc.pack()

    resultado = Label(tk, text='Resultado', fg = 'Blue')
    resultado.pack()

    tk.mainloop()
'''
from tkinter import *
import shelve

db = shelve.open('Banquito.db')

def Verifica():
    if(db['Usuarios'] == ety_Usu.get()):
        if(db['Senhas'] == ety_Sen.get()):
            msg['text'] = f'Bem vindo {ety_Usu.get()}'
            msg['fg'] = 'Green'
        else:
            msg['text'] = 'Senha Inválida'
            msg['fg'] = 'Red'
    else:
        msg['text'] = 'Usuário Inválido'
        msg['fg'] = 'Red'

#Defiine a instancia mestre
tk = Tk()

#Define o titulo e as proporções da janela
tk.title('Login')
tk.geometry('200x150')

#Bloco do Usuário
txt_Usu = Label(tk, text = 'Usuário')
ety_Usu = Entry(tk)
#------------
txt_Usu.pack()
ety_Usu.pack()

#Bloco do Login
txt_Sen = Label(tk, text = 'Senha')
ety_Sen = Entry(tk)
#------------
txt_Sen.pack()
ety_Sen.pack()

#Botão
entrar = Button(tk, text = 'Entrar', command = Verifica)
entrar.pack()

msg = Label(tk)
msg.pack()

tk.mainloop()
'''
from tkinter import *

    def Calcular():
    resultado['text'] = formula.get()
    resultado['fg'] = 'Black'

    tk = Tk()

    tk.title('Calculadora')
    tk.geometry('250x250')

    formula = Entry(tk)
    formula.pack()

    Calc = Button(tk, text = 'Calcule', command = Calcular)
    Calc.pack()

    resultado = Label(tk, text='Resultado', fg = 'Blue')
    resultado.pack()

    tk.mainloop()
'''
