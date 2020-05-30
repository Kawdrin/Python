"""Cadastro Login/Registro."""
from tkinter import *
from conts import *
from P_linhas import *
import shelve

class Tela(object):
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Login')
        self.tk.geometry(f'{ALTURA}x{LARGURA}')
        self.tk['bg'] = '#1CCEDF'

        # FRAMES
        self.f_depois_login = Frame(self.tk, bg = AZUL)
        self.f_login_e_cadastro = Frame(self.tk, bg = AZUL)
        self.f_Botoes = Frame(self.tk, bg = AZUL)
        self.f_Info = Frame(self.tk, bg = AZUL)
        # Empacotando os Frames
        self.f_login_e_cadastro.pack()
        self.f_Botoes.pack()
        self.f_Info.pack()
        self.f_depois_login.pack()

        # Bloco de login
        self.Login()
        self.LoginPack()
        #------------

        # Entrar
        b_entrar = PhotoImage(file = 'images/b_entrar.ppm')
        self.entrar = Button(self.f_Botoes, command = self.Verifica, image = b_entrar)
        self.entrar.image = b_entrar
        self.entrar.pack(side = LEFT)

        # Novo
        b_novo = PhotoImage(file = 'images/b_novo.ppm')
        self.criar = Button(self.f_Botoes, command = self.Mudar, image = b_novo)
        self.criar.image = b_novo
        self.criar.pack(side = RIGHT)

        # Informações
        self.msg = Label(self.f_Info, font = VERDANA, bg = AZUL)
        self.msg.pack()

        self.tk.mainloop()

    def Login(self):
        bg_logo = PhotoImage(file = 'images/bg_python.gif')
        self.logo = Label(self.f_login_e_cadastro)
        self.logo['image'] = bg_logo
        self.logo.image = bg_logo
        self.txt_Usu = Label(self.f_login_e_cadastro, text = 'Usuário', font = VERDANA, bg = AZUL)
        self.ety_Usu = Entry(self.f_login_e_cadastro, width = 50, font = VERDANA, bd = 5)
        self.txt_Sen = Label(self.f_login_e_cadastro, text = 'Senha', font = VERDANA, bg = AZUL)
        self.ety_Sen = Entry(self.f_login_e_cadastro, show = '*', bd = 5, width = 50, font = VERDANA)
        self.Lembrar()
        self.lembrar_select = False
        self.lembrar = Checkbutton(self.f_login_e_cadastro, text = 'Lembrar-me', font = VERDANA, bg = AZUL, command = self.VerificaLembrar)

    def LoginPack(self):
        self.logo.pack()
        self.txt_Usu.pack()
        self.ety_Usu.pack()
        self.txt_Sen.pack()
        self.ety_Sen.pack()
        self.lembrar.pack()

    def LoginPackForget(self):
        self.logo.pack_forget()
        self.txt_Usu.pack_forget()
        self.ety_Usu.pack_forget()
        self.txt_Sen.pack_forget()
        self.ety_Sen.pack_forget()
        self.lembrar.pack_forget()

    def Cadastro(self):
        self.nome_label = Label(self.f_login_e_cadastro, text = 'Nome', font = VERDANA, bg = AZUL)
        self.nome_entry = Entry(self.f_login_e_cadastro, width = 50, font = VERDANA, bd = 5)
        self.email_label = Label(self.f_login_e_cadastro, text = 'Email', font = VERDANA, bg = AZUL)
        self.email_entry = Entry(self.f_login_e_cadastro, width = 50, font = VERDANA, bd = 5)
        self.txt_Usu = Label(self.f_login_e_cadastro, text = 'Usuário', font = VERDANA, bg = AZUL)
        self.ety_Usu = Entry(self.f_login_e_cadastro, width = 50, font = VERDANA, bd = 5)
        self.txt_Sen = Label(self.f_login_e_cadastro, text = 'Senha', font = VERDANA, bg = AZUL)
        self.ety_Sen = Entry(self.f_login_e_cadastro, show = '*', bd = 5, width = 50, font = VERDANA)

    def CadastroPack(self):
        self.nome_label.pack()
        self.nome_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.txt_Usu.pack()
        self.ety_Usu.pack()
        self.txt_Sen.pack()
        self.ety_Sen.pack()

    def CadastroPackForget(self):
        self.nome_label.pack_forget()
        self.nome_entry.pack_forget()
        self.email_label.pack_forget()
        self.email_entry.pack_forget()
        self.txt_Usu.pack_forget()
        self.ety_Usu.pack_forget()
        self.txt_Sen.pack_forget()
        self.ety_Sen.pack_forget()

    def VerificaLembrar(self):
        self.lembrar_select = not self.lembrar_select
        db = shelve.open('basdasdasd.db')
        if self.lembrar_select:
            db['Lembrar'] = {'Usuario': self.ety_Usu.get(), 'Senha': self.ety_Sen.get()}
            print(db['Lembrar'])
        else:
            db['Lembrar'] = {}
            print(db['Lembrar'])
        db.close()

    def Mudar(self):
        self.LoginPackForget()
        self.entrar.pack_forget()
        self.Cadastro()
        self.CadastroPack()

        self.msg['text'] = ''

        b_criar = PhotoImage(file = 'images/b_criar.ppm')
        self.criar['image'] = b_criar
        self.criar.image = b_criar
        self.criar['command'] = self.Criar

    def Criar(self):
        if  self.ExisteDB():
            if(self.ety_Usu.get() == '') or (self.ety_Sen.get() == '') or (self.email_entry.get() == '') or (self.nome_entry.get() == ''):
                self.msg['text'] = 'Nenhum dos Campos pode estar vazio'
                self.msg['fg'] = 'Red'
            else:
                with shelve.open('basdasdasd.db') as db:
                    self.dbz = db['Cadastros']
                    self.dbz.append({'Nome': self.nome_entry.get(), 'Email': self.email_entry.get(),
                                     'Usuario': self.ety_Usu.get(), 'Senha': self.ety_Sen.get()})
                    db['Cadastros'] = self.dbz
                #
                self.CadastroPackForget()
                self.entrar.pack()
                self.Login()
                self.LoginPack()

                self.msg['text'] = 'Conta Criada'
                self.msg['fg'] = 'Green'
                #
                b_novo = PhotoImage(file = 'images/b_novo.ppm')
                self.criar['image'] = b_novo
                self.criar.image = b_novo
                #
                self.txt_Usu['text'] = 'Usuário'
                self.txt_Usu['fg'] = 'Black'
                #
                #
                self.txt_Sen['fg'] = 'Black'
                self.criar['command'] = self.Mudar

    def Verifica(self):
        if self.ExisteDB():
            with shelve.open('basdasdasd.db') as db:
                self.logins = db['Cadastros']
                for l in self.logins:
                    if(l['Usuario'] == self.ety_Usu.get()):
                        if(l['Senha'] != self.ety_Sen.get()):
                            self.msg['text'] = 'Senha Inválida'
                            self.msg['fg'] = 'Red'
                        else:
                            db.close()
                            self.ForgetVerificar()
                            self.BotoesLogin()
                            return
                    else:
                        self.msg['text'] = 'Usuário Inválido'
                        self.msg['fg'] = 'Red'

    def ForgetVerificar(self):
        self.LoginPackForget()
        self.logo.pack_forget()
        self.entrar.pack_forget()
        self.criar.pack_forget()
        self.msg.pack_forget()
        self.f_Botoes.pack_forget()
        self.f_Info.pack_forget()
        self.f_login_e_cadastro.pack_forget()

    def BotoesLogin(self):
        self.tk.geometry('170x120')
        self.b_canva_pintar_linhas = Button(self.f_depois_login, text = 'Apps Canvas 1 - linhas', command = self.PintarLinha)
        self.b_canva_pintar_linhas.pack()

        self.b_canvas_pintar_poly = Button(self.f_depois_login, text = 'Apps Canvas 2 - Polygons', command = self.PintarPoly)
        self.b_canvas_pintar_poly.pack()

        self.b_canvas_carinha = Button(self.f_depois_login, text = 'Apps Canvas 3 - Carinha', command = self.PintarCara)
        self.b_canvas_carinha.pack()

        self.b_canvas_mario = Button(self.f_depois_login, text = 'Apps Canvas 4 - Mario', command = self.PintarMariozin)
        self.b_canvas_mario.pack()

    def PintarLinha(self):
        self.f_depois_login.pack_forget()
        PintarLinhas(self.tk)

    def PintarPoly(self):
        self.f_depois_login.pack_forget()
        PintarPolygon(self.tk)

    def PintarCara(self):
        self.f_depois_login.pack_forget()
        PintarCarinha(self.tk)

    def PintarMariozin(self):
        self.f_depois_login.pack_forget()
        PintarMario(self.tk)

    def ExisteDB(self):
        db = shelve.open('basdasdasd.db')
        try:
            self.verifica_db = db['Cadastros']
        except:
            db['Cadastros'] = []
            db['Lembrar'] = {}
        finally:
            db.close()
            return True

    def Lembrar(self):
        db = shelve.open('basdasdasd.db')
        try:
            self.ety_Usu.insert(END, db['Lembrar']['Usuario'])
            self.ety_Sen.insert(END, db['Lembrar']['Senha'])
        except:
            self.ety_Usu.insert(END, '')
            self.ety_Sen.insert(END, '')
        finally:
            db.close()


#Defiine a instancia mestre
Tela()

#Define o titulo e as proporções da janela
