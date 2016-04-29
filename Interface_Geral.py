import tkinter as tk

class Tela_Login:
    def __init__(self):
        #importa classe Armazenamento
        self.am = Armazenamento()
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
        
        #Criando selfs de cadastrar
        self.preco = ""
        self.preco_st = tk.StringVar()
        
        self.troca = ""
        self.troca_st = tk.StringVar()
        
        self.descricao = ""
        self.descricao_st = tk.StringVar()
        
        self.produto = ""
        self.produto_st = tk.StringVar()
        
        self.senha_cad = ""
        self.senha_cad_st = tk.StringVar()
        
        self.senha_log = ""
        self.senha_log_st = tk.StringVar()
                
        self.email = ""
        self.email_st = tk.StringVar()
        
        self.user_cad = ""
        self.user_cad_st = tk.StringVar()
        
        self.user_log = ""
        self.user_log_st = tk.StringVar()
        
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
        self.login_user_cx.configure(font="Courier 25 bold", textvariable = self.user_log_st)
        
        
        #Label Login Senha
        self.login_senha = tk.Label(self.window)
        self.login_senha.grid(row=2, column=0, sticky="nsw")
        self.login_senha.configure(text=" Senha: ")
        self.login_senha.configure(font="Courier 40 bold")
        
        #Entery Login Senha
        self.login_senha_cx = tk.Entry(self.window)
        self.login_senha_cx.grid(row=2, column=1, columnspan=3, sticky="w")
        self.login_senha_cx.configure(font="Courier 25 bold", textvariable = self.senha_log_st)
        
        #Botão Login
        self.enter_login = tk.Button(self.window)
        self.enter_login.configure(text=" Login ", command=self.s0e1)
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
        self.cadastro_user_cx.configure(font="Courier 25 bold" , textvariable = self.user_cad_st)
        
        #Label Cadastro Email
        self.cadastro_email = tk.Label(self.window)
        self.cadastro_email.grid(row=5, column=0, sticky="nsw")
        self.cadastro_email.configure(text=" E-mail: ")
        self.cadastro_email.configure(font="Courier 40 bold")
        
        #Entery Cadastro Email
        self.cadastro_email_cx = tk.Entry(self.window)
        self.cadastro_email_cx.grid(row=5, column=1, columnspan=3, sticky="w")
        self.cadastro_email_cx.configure(font="Courier 25 bold" , textvariable = self.email_st)
        
        #Label Cadastro Senha
        self.cadastro_senha = tk.Label(self.window)
        self.cadastro_senha.grid(row=6, column=0, sticky="nsw")
        self.cadastro_senha.configure(text=" Senha: ")
        self.cadastro_senha.configure(font="Courier 40 bold")
        
        #Entery Cadastro Senha
        self.cadastro_senha_cx = tk.Entry(self.window)
        self.cadastro_senha_cx.grid(row=6, column=1, columnspan=3, sticky="w")
        self.cadastro_senha_cx.configure(font="Courier 25 bold" , textvariable = self.senha_cad_st)
        
        #Botão Cadastro
        self.enter_cadastro = tk.Button(self.window)
        self.enter_cadastro.configure(text=" Cadastro ", command=self.s0e1)
        self.enter_cadastro.grid(row=6, column=4, columnspan=6)
        self.enter_cadastro.configure(font="Courier 25 bold")      
        
    def primeira_pagina(self):
         #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Trade Market",command=self.s1e1)
        self.slogan.configure(font="Courier 50 bold")
        
         #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)
        self.user_name.grid(row=0, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(text= self.user_log,command=self.s1e2)
        self.user_name.configure(font="Courier 30 bold")
        
        #Label Feed produtos
        self.feed_produtos = tk.Label(self.window)
        self.feed_produtos.grid(row=2, column=0, columnspan=3, sticky="nsw")
        self.feed_produtos.configure(text=" Feed Produtos")
        self.feed_produtos.configure(font="Courier 50 bold")
        
        #Botao Produto_1        
        self.botao_produto_1 = tk.Button(self.window)
        self.botao_produto_1.grid(row=3, column=0, columnspan=3, sticky="nsew")
        self.botao_produto_1.configure(text=" Livro de Calculo 1 \n Valor: R$60,00 \n Troca: Calculadora ",command=self.s1e3)
        self.botao_produto_1.configure(font="Courier 15 bold")
        
        #Botao Produto_2        
        self.botao_produto_2 = tk.Button(self.window)
        self.botao_produto_2.grid(row=4, column=0, columnspan=3, sticky="nsew")
        self.botao_produto_2.configure(text=" LCD 2X16 \n Valor: R$40,00 \n Troca: LM35 (sensor de temp) ",command=self.s1e3)
        self.botao_produto_2.configure(font="Courier 15 bold")
        
        #Botao Produto_3        
        self.botao_produto_3 = tk.Button(self.window)
        self.botao_produto_3.grid(row=5, column=0, columnspan=3, sticky="nsew")
        self.botao_produto_3.configure(text=" Protoboard \n Valor: R$30,00 \n Troca: Arduino (mais volta minha!!) ",command=self.s1e3)
        self.botao_produto_3.configure(font="Courier 15 bold")
        
    def segunda_pagina(self):
        #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Trade Market",command=self.s2e1)
        self.slogan.configure(font="Courier 50 bold")
        
         #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)
        self.user_name.grid(row=0, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(text= self.user_log,command=self.s2e2)
        self.user_name.configure(font="Courier 30 bold")
        
        #Label Cadastrar Produtos
        self.cadastrar_produtos = tk.Label(self.window)
        self.cadastrar_produtos.grid(row=2, column=0, columnspan=3, sticky="nsw")
        self.cadastrar_produtos.configure(text=" Cadastrar Produtos")
        self.cadastrar_produtos.configure(font="Courier 30 bold")
        
        #Label Nome produto
        self.nome_produto = tk.Label(self.window)
        self.nome_produto.grid(row=3, column=0, columnspan=3, sticky="nsw")
        self.nome_produto.configure(text=" Nome:")
        self.nome_produto.configure(font="Courier 20 bold")
        
        #Entery Nome produto
        self.nome_produto_cx = tk.Entry(self.window)
        self.nome_produto_cx.grid(row=3, column=1, columnspan=3, sticky="w")
        self.nome_produto_cx.configure(font="Courier 25 bold" , textvariable = self.produto_st)
        
        #Label Preco produto
        self.preco_produto = tk.Label(self.window)
        self.preco_produto.grid(row=4, column=0, columnspan=3, sticky="nsw")
        self.preco_produto.configure(text=" Preço:")
        self.preco_produto.configure(font="Courier 20 bold")
        
        #Entery Preco Produto
        self.preco_produto_cx = tk.Entry(self.window)
        self.preco_produto_cx.grid(row=4, column=1, columnspan=3, sticky="w")
        self.preco_produto_cx.configure(font="Courier 25 bold" , textvariable = self.preco_st)
        
        #Label Troca Produto
        self.troca_produto = tk.Label(self.window)
        self.troca_produto.grid(row=5, column=0, columnspan=3, sticky="nsw")
        self.troca_produto.configure(text=" Troca:")
        self.troca_produto.configure(font="Courier 20 bold")
        
        #Entery Troca Produto
        self.troca_produto_cx = tk.Entry(self.window)
        self.troca_produto_cx.grid(row=5, column=1, columnspan=3, sticky="w")
        self.troca_produto_cx.configure(font="Courier 25 bold" , textvariable = self.troca_st)
        
        #Label Meus Produtos Anunciados
        self.meus_produtos_anun = tk.Label(self.window)
        self.meus_produtos_anun.grid(row=2, column=3, columnspan=6, sticky="nsw")
        self.meus_produtos_anun.configure(text=" Meus Produtos Anunciados")
        self.meus_produtos_anun.configure(font="Courier 30 bold")
        
        #Botao Produto_1        
        self.botao_meuproduto_1 = tk.Button(self.window)
        self.botao_meuproduto_1.grid(row=3, column=3, columnspan=6, sticky="nsew")
        self.botao_meuproduto_1.configure(text=" Livro de Calculo 1 \n Valor: R$60,00 \n Troca: Calculadora ",command=self.s2e3)
        self.botao_meuproduto_1.configure(font="Courier 15 bold")
        
        #Botao Produto_2        
        self.botao_meuproduto_2 = tk.Button(self.window)
        self.botao_meuproduto_2.grid(row=4, column=3, columnspan=6, sticky="nsew")
        self.botao_meuproduto_2.configure(text=" LCD 2X16 \n Valor: R$40,00 \n Troca: LM35 (sensor de temp) ",command=self.s2e3)
        self.botao_meuproduto_2.configure(font="Courier 15 bold")
        
        #Botao Produto_3        
        self.botao_meuproduto_3 = tk.Button(self.window)
        self.botao_meuproduto_3.grid(row=5, column=3, columnspan=6, sticky="nsew")
        self.botao_meuproduto_3.configure(text=" Protoboard \n Valor: R$30,00 \n Troca: Arduino (mais volta minha!!) ",command=self.s2e3)
        self.botao_meuproduto_3.configure(font="Courier 15 bold")
        
        #Botao confirmar
        self.botao_confirmar=tk.Button(self.window)
        self.botao_confirmar.grid(row=6, column=0, sticky="nsew")
        self.botao_confirmar.configure(text="confirmar", font="Courier 15 bold",command=self.s2e2 )
        
    def terceira_pagina(self):
        #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Trade Market",command=self.s3e1)
        self.slogan.configure(font="Courier 50 bold")
        
         #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)
        self.user_name.grid(row=0, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(text= self.user_log,command=self.s3e2)
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
        self.info_preco_produto = tk.Label(self.window)
        self.info_preco_produto.grid(row=3, column=3, columnspan=6, sticky="nsw")
        self.info_preco_produto.configure(text="Preço: R$60,00 \n \n Troca: Calculadora")
        self.info_preco_produto.configure(font="Courier 15 bold")
        
        #Label Email
        self.info_email_produto = tk.Label(self.window)
        self.info_email_produto.grid(row=4, column=3, columnspan=6, sticky="nsw")
        self.info_email_produto.configure(text="Email: vendedor.exemplo@gmail.com")
        self.info_email_produto.configure(font="Courier 15 bold")        
        
    def iniciar(self):
        self.window.mainloop()
        
    def nome_st (self):
        self.user_log = self.user_log_st.get()
        self.senha_log = self.senha_log_st.get()
        self.user_cad = self.user_cad_st.get()
        self.senha_cad = self.senha_cad_st.get()
        self.email = self.email_st.get()
        
    def limpar_0(self):
        self.slogan.grid_forget()
        self.login.grid_forget()
        self.login_user.grid_forget()
        self.login_senha.grid_forget()
        self.login_user_cx.grid_forget()
        self.login_senha_cx.grid_forget()
        self.enter_login.grid_forget()
        self.cadastro.grid_forget()
        self.cadastro_user.grid_forget()
        self.cadastro_user_cx.grid_forget()
        self.cadastro_email.grid_forget()
        self.cadastro_email_cx.grid_forget()
        self.cadastro_senha.grid_forget()
        self.cadastro_senha_cx.grid_forget()
        self.enter_cadastro.grid_forget()
        self.nome_st()
        self.am.cadastro_geral()
        
    def limpar_1(self):
        self.slogan.grid_forget()
        self.user_name.grid_forget()
        self.feed_produtos.grid_forget()
        self.botao_produto_1.grid_forget()
        self.botao_produto_2.grid_forget()
        self.botao_produto_3.grid_forget()
        
    def limpar_2(self):
        self.slogan.grid_forget()
        self.user_name.grid_forget()
        self.cadastrar_produtos.grid_forget()
        self.nome_produto.grid_forget()
        self.preco_produto.grid_forget()
        self.nome_produto_cx.grid_forget()
        self.preco_produto_cx.grid_forget()
        self.troca_produto.grid_forget()
        self.troca_produto_cx.grid_forget()
        self.meus_produtos_anun.grid_forget()
        self.botao_meuproduto_1.grid_forget()
        self.botao_meuproduto_2.grid_forget()
        self.botao_meuproduto_3.grid_forget()
        self.botao_confirmar.grid_forget()
        
    def limpar_3(self):
        self.slogan.grid_forget()
        self.user_name.grid_forget()
        self.foto_produto.grid_forget()
        self.descricao_produto.grid_forget()
        self.info_preco_produto.grid_forget()
        self.info_email_produto.grid_forget()
        
    def pagina_1(self):
       self.primeira_pagina()
        
    def pagina_2(self):
        self.segunda_pagina()
        
    def pagina_3(self):
        self.terceira_pagina()
    
    def s0e1(self):
        self.limpar_0()
        self.pagina_1()
        
    def s1e1(self):
        self.limpar_1()
        self.pagina_1()
        
    def s1e2(self):
        self.limpar_1()
        self.pagina_2()
        
    def s1e3(self):
        self.limpar_1()
        self.pagina_3()
        
    def s2e1(self):
        self.limpar_2()
        self.pagina_1()
    
    def s2e2(self):
        self.limpar_2()
        self.pagina_2()
        
    def s2e3(self):
        self.limpar_2()
        self.pagina_3()
        
    def s3e1(self):
        self.limpar_3()
        self.pagina_1()
        
    def s3e2(self):
        self.limpar_3()
        self.pagina_2()

class Armazenamento:
    def __init__(self):
        #importando classe Tela Login
        self.tela = Tela_Login()
        # criando os dicionarios
        self.user_dic = {}
        self.lista_user = []
        self.produto_dic = {}
        self.lista_produto = []
    
        #criando asfunções de callback
        def cadastro_geral(self):
            self.lista_user.append(self.tela.email)
            self.lista_user.append(self.tela.senha_cad)
            self.user_dic[self.tela.user_cad]=self.lista_user
            print(self.user_dic)
            
Site = Tela_Login()
Site.iniciar()  