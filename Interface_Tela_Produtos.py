# -*- coding: utf-8 -*-
import tkinter as tk

class Tela_Produtos:
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
        
        #Label Feed produtos
        self.feed_produtos = tk.Label(self.window)
        self.feed_produtos.grid(row=2, column=0, columnspan=3, sticky="nsw")
        self.feed_produtos.configure(text=" Feed Produtos")
        self.feed_produtos.configure(font="Courier 50 bold")
        
        #Botao Produto_1        
        self.botao_produto_1 = tk.Button(self.window)
        self.botao_produto_1.grid(row=3, column=0, columnspan=3, sticky="nsew")
        self.botao_produto_1.configure(text=" Livro de Calculo 1 \n Valor: R$60,00 \n Troca: Calculadora ")
        self.botao_produto_1.configure(font="Courier 15 bold")
        
        #Botao Produto_2        
        self.botao_produto_2 = tk.Button(self.window)
        self.botao_produto_2.grid(row=4, column=0, columnspan=3, sticky="nsew")
        self.botao_produto_2.configure(text=" LCD 2X16 \n Valor: R$40,00 \n Troca: LM35 (sensor de temp) ")
        self.botao_produto_2.configure(font="Courier 15 bold")
        
        #Botao Produto_3        
        self.botao_produto_3 = tk.Button(self.window)
        self.botao_produto_3.grid(row=5, column=0, columnspan=3, sticky="nsew")
        self.botao_produto_3.configure(text=" Protoboard \n Valor: R$30,00 \n Troca: Arduino (mais volta minha!!) ")
        self.botao_produto_3.configure(font="Courier 15 bold")
        
        
        
        
    def iniciar(self):
        self.window.mainloop()
        
    

Site = Tela_Produtos()
Site.iniciar()  