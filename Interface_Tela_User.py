# -*- coding: utf-8 -*-
import tkinter as tk

class Tela_User:
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
        
        #Label Cadastrar Produtos
        self.feed_produtos = tk.Label(self.window)
        self.feed_produtos.grid(row=2, column=0, columnspan=3, sticky="nsw")
        self.feed_produtos.configure(text=" Cadastrar Produtos")
        self.feed_produtos.configure(font="Courier 30 bold")
        
        #Label Nome produto
        self.nome_produto = tk.Label(self.window)
        self.nome_produto.grid(row=3, column=0, columnspan=3, sticky="nsw")
        self.nome_produto.configure(text=" Nome:")
        self.nome_produto.configure(font="Courier 20 bold")
        
        #Entery Nome produto
        self.nome_produto_cx = tk.Entry(self.window)
        self.nome_produto_cx.grid(row=3, column=1, columnspan=3, sticky="w")
        self.nome_produto_cx.configure(font="Courier 25 bold")
        
        #Label Preco produto
        self.preco_produto = tk.Label(self.window)
        self.preco_produto.grid(row=4, column=0, columnspan=3, sticky="nsw")
        self.preco_produto.configure(text=" Preço:")
        self.preco_produto.configure(font="Courier 20 bold")
        
        #Entery Preco Produto
        self.preco_produto_cx = tk.Entry(self.window)
        self.preco_produto_cx.grid(row=4, column=1, columnspan=3, sticky="w")
        self.preco_produto_cx.configure(font="Courier 25 bold")
        
        #Label Troca Produto
        self.troca_produto = tk.Label(self.window)
        self.troca_produto.grid(row=5, column=0, columnspan=3, sticky="nsw")
        self.troca_produto.configure(text=" Troca:")
        self.troca_produto.configure(font="Courier 20 bold")
        
        #Entery Troca Produto
        self.troca_produto_cx = tk.Entry(self.window)
        self.troca_produto_cx.grid(row=5, column=1, columnspan=3, sticky="w")
        self.troca_produto_cx.configure(font="Courier 25 bold")
        
        #Label Meus Produtos Anunciados
        self.meus_produtos_anun = tk.Label(self.window)
        self.meus_produtos_anun.grid(row=2, column=3, columnspan=6, sticky="nsw")
        self.meus_produtos_anun.configure(text=" Meus Produtos Anunciados")
        self.meus_produtos_anun.configure(font="Courier 30 bold")
        
        #Botao Produto_1        
        self.botao_produto_1 = tk.Button(self.window)
        self.botao_produto_1.grid(row=3, column=3, columnspan=6, sticky="nsew")
        self.botao_produto_1.configure(text=" Livro de Calculo 1 \n Valor: R$60,00 \n Troca: Calculadora ")
        self.botao_produto_1.configure(font="Courier 15 bold")
        
        #Botao Produto_2        
        self.botao_produto_2 = tk.Button(self.window)
        self.botao_produto_2.grid(row=4, column=3, columnspan=6, sticky="nsew")
        self.botao_produto_2.configure(text=" LCD 2X16 \n Valor: R$40,00 \n Troca: LM35 (sensor de temp) ")
        self.botao_produto_2.configure(font="Courier 15 bold")
        
        #Botao Produto_3        
        self.botao_produto_3 = tk.Button(self.window)
        self.botao_produto_3.grid(row=5, column=3, columnspan=6, sticky="nsew")
        self.botao_produto_3.configure(text=" Protoboard \n Valor: R$30,00 \n Troca: Arduino (mais volta minha!!) ")
        self.botao_produto_3.configure(font="Courier 15 bold")
        
    def iniciar(self):
        self.window.mainloop()
        
    

Site = Tela_User()
Site.iniciar()  