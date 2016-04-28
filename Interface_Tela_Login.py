# -*- coding: utf-8 -*-
import tkinter as tk

class Tela_Login:
    def __init__(self):
        #Interface
        self.window = tk.Tk()
        self.window.title("Troca e Venda")
        self.window.geometry("1300x700")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=100, weight=1)
        self.window.rowconfigure(4, minsize=100, weight=1)
        self.window.rowconfigure(5, minsize=100, weight=1)
        self.window.rowconfigure(6, minsize=100, weight=1)
        self.window.columnconfigure(0, minsize=200, weight=1)
        self.window.columnconfigure(1, minsize=200, weight=1)
        self.window.columnconfigure(2, minsize=200, weight=1)
        self.window.columnconfigure(3, minsize=200, weight=1)
        self.window.columnconfigure(4, minsize=200, weight=1)
        self.window.columnconfigure(5, minsize=200, weight=1)
        
        #Label Slogan
        self.slogan = tk.Label(self.window)
        self.slogan.grid(row=0, column=3, columnspan=6, sticky="nsw")
        self.slogan.configure(text="Trade Market")
        self.slogan.configure(font="Courier 60 bold")
        
        #Label Login
        self.login = tk.Label(self.window)
        self.login.grid(row=0, column=0, columnspan=2, sticky="nsw")
        self.login.configure(text=" Login")
        self.login.configure(font="Courier 70 bold")
        
        #Label Login User
        self.login_user = tk.Label(self.window)
        self.login_user.grid(row=1, column=0, sticky="nsw")
        self.login_user.configure(text=" User: ")
        self.login_user.configure(font="Courier 40 bold")
        
        #Entery Login User
        self.login_user_cx = tk.Entry(self.window)
        self.login_user_cx.grid(row=1, column=1, columnspan=3, sticky="w")
        self.login_user_cx.configure(font="Courier 25 bold")
        
        
        #Label Login Senha
        self.login_senha = tk.Label(self.window)
        self.login_senha.grid(row=2, column=0, sticky="nsw")
        self.login_senha.configure(text=" Senha: ")
        self.login_senha.configure(font="Courier 40 bold")
        
        #Entery Login Senha
        self.login_senha_cx = tk.Entry(self.window)
        self.login_senha_cx.grid(row=2, column=1, columnspan=3, sticky="w")
        self.login_senha_cx.configure(font="Courier 25 bold")
        
        #Botão Login
        self.enter_login = tk.Button(self.window)
        self.enter_login.configure(text=" Login ")
        self.enter_login.grid(row=2, column=4, columnspan=6)
        self.enter_login.configure(font="Courier 25 bold")
        
        #Label Cadastro
        self.cadastro = tk.Label(self.window)
        self.cadastro.grid(row=3, column=0, columnspan=2, stick="nsw")
        self.cadastro.configure(text=" Cadastro")
        self.cadastro.configure(font="Courier 70 bold")
        
        #Label Cadastro User
        self.cadastro_user = tk.Label(self.window)
        self.cadastro_user.grid(row=4, column=0, sticky="nsw")
        self.cadastro_user.configure(text=" User: ")
        self.cadastro_user.configure(font="Courier 40 bold")
        
        #Entery Cadastro User
        self.cadastro_user_cx = tk.Entry(self.window)
        self.cadastro_user_cx.grid(row=4, column=1, columnspan=3, sticky="w")
        self.cadastro_user_cx.configure(font="Courier 25 bold")
        
        #Label Cadastro Email
        self.cadastro_email = tk.Label(self.window)
        self.cadastro_email.grid(row=5, column=0, sticky="nsw")
        self.cadastro_email.configure(text=" E-mail: ")
        self.cadastro_email.configure(font="Courier 40 bold")
        
        #Entery Cadastro Email
        self.cadastro_email_cx = tk.Entry(self.window)
        self.cadastro_email_cx.grid(row=5, column=1, columnspan=3, sticky="w")
        self.cadastro_email_cx.configure(font="Courier 25 bold")
        
        #Label Cadastro Senha
        self.cadastro_senha = tk.Label(self.window)
        self.cadastro_senha.grid(row=6, column=0, sticky="nsw")
        self.cadastro_senha.configure(text=" Senha: ")
        self.cadastro_senha.configure(font="Courier 40 bold")
        
        #Entery Cadastro Senha
        self.cadastro_senha_cx = tk.Entry(self.window)
        self.cadastro_senha_cx.grid(row=6, column=1, columnspan=3, sticky="w")
        self.cadastro_senha_cx.configure(font="Courier 25 bold")
        
        #Botão Cadastro
        self.enter_cadastro = tk.Button(self.window)
        self.enter_cadastro.configure(text=" Cadastro ")
        self.enter_cadastro.grid(row=6, column=4, columnspan=6)
        self.enter_cadastro.configure(font="Courier 25 bold")        
        
    def iniciar(self):
        self.window.mainloop()
        
    

Site = Tela_Login()
Site.iniciar()  