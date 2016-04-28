# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import tkinter as tk

class Tela_Comprar_Produto:
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
        self.window.rowconfigure(7, minsize=100, weight=1)
        self.window.rowconfigure(8, minsize=100, weight=1)
        self.window.rowconfigure(9, minsize=100, weight=1)
        self.window.rowconfigure(10, minsize=100, weight=1)
        self.window.columnconfigure(0, minsize=200, weight=1)
        self.window.columnconfigure(1, minsize=200, weight=1)
        self.window.columnconfigure(2, minsize=200, weight=1)
        self.window.columnconfigure(3, minsize=200, weight=1)
        self.window.columnconfigure(4, minsize=200, weight=1)
        self.window.columnconfigure(5, minsize=200, weight=1)
        
#        #Scrollbar
#        self.scrollbar = tk.Scrollbar(self.window)
#        self.scrollbar.pack(side="right", fill="y")
        
         #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Trade Market")
        self.slogan.configure(font="Courier 50 bold")
        
         #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)
        self.user_name.grid(row=0, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(text=" Nome User ")
        self.user_name.configure(font="Courier 30 bold")
        
        #Label Foto Produto
        self.foto_produto = tk.Label(self.window)
        self.foto_produto.grid(row=2, rowspan=4, column=0, columnspan=2, sticky="nsw")
        self.foto_produto.configure(text="Foto",font="Courier 200 bold",bg="red")
        
        #Label Descrição Produto
        self.descricao_produto = tk.Label(self.window)
        self.descricao_produto.grid(row=2, column=3, columnspan=6, sticky="nsw")
        self.descricao_produto.configure(text="Nome: LCD 2x16 \n \n Descrição: Ótimo estado")
        self.descricao_produto.configure(font="Courier 15 bold")
        
        #Label Preco Troca Produto
        self.descricao_produto = tk.Label(self.window)
        self.descricao_produto.grid(row=3, column=3, columnspan=6, sticky="nsw")
        self.descricao_produto.configure(text="Preço: R$60,00 \n \n Troca: Calculadora")
        self.descricao_produto.configure(font="Courier 15 bold")
        
        #Label Email
        self.descricao_produto = tk.Label(self.window)
        self.descricao_produto.grid(row=4, column=3, columnspan=6, sticky="nsw")
        self.descricao_produto.configure(text="Email: vendedor.exemplo@gmail.com")
        self.descricao_produto.configure(font="Courier 15 bold")
                
        
    def iniciar(self):
        self.window.mainloop()
        
    

Site = Tela_Comprar_Produto()
Site.iniciar()  
