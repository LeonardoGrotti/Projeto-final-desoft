from firebase import firebase
import tkinter as tk
import smtplib
#from validate_email import validate_email
from PIL import ImageTk, Image



class Tela_Login:
    def __init__(self):
        #firebase
        self.fb = firebase.FirebaseApplication("https://trocavenda.firebaseio.com/")
        
        #Interface
        self.window = tk.Tk()
        self.window.title("Troca e Venda")
        self.window.geometry("{0}x{1}".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.rowconfigure(0, minsize=40, weight=1)
        self.window.rowconfigure(1, minsize=40, weight=1)
        self.window.rowconfigure(2, minsize=20, weight=1)
        self.window.rowconfigure(3, minsize=100, weight=1)
        self.window.rowconfigure(4, minsize=100, weight=1)
        self.window.rowconfigure(5, minsize=100, weight=1)
        self.window.rowconfigure(6, minsize=100, weight=1)
        self.window.rowconfigure(7, minsize=100, weight=1)
        self.window.rowconfigure(8, minsize=100, weight=1)
        self.window.columnconfigure(0, minsize=200, weight=1)
        self.window.columnconfigure(1, minsize=200, weight=1)
        self.window.columnconfigure(2, minsize=200, weight=1)
        self.window.columnconfigure(3, minsize=200, weight=1)
        self.window.columnconfigure(4, minsize=200, weight=1)
        self.window.columnconfigure(5, minsize=200, weight=1)
        
        #CORES
        self.window.configure(bg= "white")
        
        #Baita Variavel necessaria
        self.A = -1
        self.nome_excluir=0
        
        #Label Login Fail
        self.login_fail = tk.Label()
        self.login_fail.grid(row=7, column=4, sticky="nsew")
        self.login_fail.configure(text="", bg= "white")
    
        self.login_fail1 = tk.Label()
        self.login_fail1.grid(row=0, column=5, columnspan=6, sticky="wnse")
        self.login_fail1.configure(text="" ,bg= "chartreuse3")
        
        #lista de todos os produtos de todos os usuários
        L = self.fb.get("todos_os_produtos/geral","top")
        if L == None:
            self.t_prod_u = []
        else:
            self.t_prod_u = L
        
        self.zero_pagina()
        
        #lista de todos os produtos de um usuário
        self.lista_prod_tot = []
        
        #dic dos produtos
        self.produto_user = {}
        
        # variável de pesquisa
        self.p = 0
                
    #Criando paginas
        
    def zero_pagina(self):
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
                
        #linha em baixo do nome do site
        self.mini_linha = tk.Label(self.window)
        self.mini_linha.grid(row=2, column=0, columnspan=6, sticky="nsew")
        self.mini_linha.configure(text="Desenvolvido por : Caue Citrin, Leonardo Grotti, Patrick Wiegeneric, Rodrigo Lino. Participações especiais: Fabio Ayres e Camila. Por um mundo mais sustentável",font="Times 10 bold" ,bg="gray18",fg="white")
       
           #Label de cor
        self.label_1 =tk.Label(self.window)
        self.label_1.grid(row=0, rowspan=2, column=1, columnspan=4, sticky="nsew")
        self.label_1.configure(bg="chartreuse3")
               
       
        #Label Slogan
        self.slogan = tk.Label(self.window)
        self.slogan.grid(row=0, rowspan=2, column=0, columnspan=2, sticky="nws")
        self.slogan.configure(text="Save & Trade",font="Times 60 bold" ,bg="chartreuse3",fg="gray18")
       
     
        #Label de cor 2
        self.label_1 =tk.Label(self.window)
        self.label_1.grid(row=1, column=2, columnspan=6, sticky="nsew")
        self.label_1.configure(bg="chartreuse3")        
        
        #Label Login
        self.login = tk.Label(self.window)
        self.login.grid(row=0, rowspan=1, column=3, columnspan=4, sticky="nsw")
        self.login.configure(text=" Login:",font="Times 30 bold",bg="chartreuse3",fg="gray18")
        
        
        #Entery Login User
        self.login_user_cx = tk.Entry(self.window)
        self.login_user_cx.grid(row=0, column=4, columnspan=5, sticky="w")
        self.login_user_cx.configure(font="Times 20 bold", textvariable = self.user_log_st)
        
        
        #Label Login Senha
        self.login_senha = tk.Label(self.window)
        self.login_senha.grid(row=1, column=3, columnspan=4, sticky="nsw")
        self.login_senha.configure(text=" Senha: " ,font="Times 30 bold",bg="chartreuse3", fg="gray18")
        
        #Entery Login Senha
        self.login_senha_cx = tk.Entry(self.window)
        self.login_senha_cx.grid(row=1, column=4, columnspan=5, sticky="w")
        self.login_senha_cx.configure(font="Times 20 bold", textvariable = self.senha_log_st,show="*" )
        self.login_senha_cx.bind("<Return>",self.s0e1_log_enter)
        
        #Botão Login
        self.enter_login = tk.Button(self.window)
        self.enter_login.configure(text=" Login ", command=self.s0e1_log, font="Times 20 bold", bg= "white")
        self.enter_login.grid(row=1, column=5, columnspan=6, sticky="e")
        self.enter_login.bind("<Return>",self.s0e1_log_enter)
        
        #Label Cadastro
        self.cadastro = tk.Label(self.window)
        self.cadastro.grid(row=3, column=3, columnspan=4, sticky="ew")
        self.cadastro.configure(text=" Cadastro", font="Times 70 bold",bg= "white")
        
        
        #Label Cadastro User
        self.cadastro_user = tk.Label(self.window)
        self.cadastro_user.grid(row=4, column=3, columnspan=4, sticky="nsw")
        self.cadastro_user.configure(text=" User: ", font="Times 40 bold",bg= "white")
        
        #Entery Cadastro User
        self.cadastro_user_cx = tk.Entry(self.window)
        self.cadastro_user_cx.grid(row=4, column=4, columnspan=5, sticky="w")
        self.cadastro_user_cx.configure(font="Times 25 bold" , textvariable = self.user_cad_st)
        
        #Label Cadastro Email
        self.cadastro_email = tk.Label(self.window)
        self.cadastro_email.grid(row=5, column=3, columnspan=4, sticky="nsw")
        self.cadastro_email.configure(text=" E-mail: ", font="Times 40 bold",bg= "white")
      
        #Entery Cadastro Email
        self.cadastro_email_cx = tk.Entry(self.window)
        self.cadastro_email_cx.grid(row=5, column=4, columnspan=5, sticky="w")
        self.cadastro_email_cx.configure(font="Times 25 bold" , textvariable = self.email_st)
        
        #Label Cadastro Senha
        self.cadastro_senha = tk.Label(self.window)
        self.cadastro_senha.grid(row=6, column=3, columnspan=4, sticky="nsw")
        self.cadastro_senha.configure(text=" Senha: ", font="Times 40 bold",bg= "white")
        
        #Entery Cadastro Senha
        self.cadastro_senha_cx = tk.Entry(self.window)
        self.cadastro_senha_cx.grid(row=6, column=4, columnspan=5, sticky="w")
        self.cadastro_senha_cx.configure(font="Times 25 bold" , textvariable = self.senha_cad_st,show="*" )
        self.cadastro_senha_cx.bind("<Return>",self.s0e1_cad_enter)
        
        #Botão Cadastro
        self.enter_cadastro = tk.Button(self.window)
        self.enter_cadastro.configure(text=" Cadastro ", command=self.s0e1_cad, font="Times 25 bold",bg= "white")
        self.enter_cadastro.grid(row=7, column=5, columnspan=6) 
        self.enter_cadastro.bind("<Return>",self.s0e1_cad_enter)
        
        #Foto
        self.diretorio ="etiqueta.jpg"
        self.img = ImageTk.PhotoImage(Image.open(self.diretorio))

        self.imglabel = tk.Label(self.window, image=self.img) 
        self.imglabel.grid(row=3, rowspan=6, column=0, columnspan=3)

    def primeira_pagina(self):
        
        self.search = ""
        self.search_st = tk.StringVar()
        
        #Botao search
        self.botao_search = tk.Button(self.window)
        self.botao_search.grid(row=3, column=0, sticky="ew")
        self.botao_search.configure(command=self.search_play, font="Times 25 bold", text="Pesquisar")
        
        #Entry search
        self.search_cx = tk.Entry(self.window)
        self.search_cx.grid(row=3, column=1, sticky="e")
        self.search_cx.configure(font="Times 25 bold", textvariable = self.search_st, bg="white")
        self.search_cx.bind("<Return>", self.apertou_enter_pesquisa)
        
        #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Save & Trade", command=self.s1e1,font="Times 60 bold", bg="chartreuse3",fg="gray18")
        
        #linha em baixo do nome do site
        self.mini_linha = tk.Label(self.window)
        self.mini_linha.grid(row=2, column=0, columnspan=7, sticky="nsew")
        self.mini_linha.configure(text="Desenvolvido por : Caue Citrin, Leonardo Grotti, Patrick Wiegeneric, Rodrigo Lino. Participações especiais: Fabio Ayres e Camila. Por um mundo mais sustentável",font="Times 10 bold" ,bg="gray18",fg="white")
         
        #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)     
        self.user_name.grid(row=0, rowspan=2, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(command=self.s1e2,text="Meus produtos", font="Times 30 bold", bg = "chartreuse3",fg="gray18")
        
        #Botao Logout
        self.botao_logout = tk.Button(self.window)
        self.botao_logout.grid(row=8,column=6)
        self.botao_logout.configure(text="Logout", command=self.s1e0,font="Times 18 bold",bg= "white")
        self.botao_logout.bind("<Return>", self.s1e0_enter)
        
        #Label Feed produtos
        self.feed_produtos = tk.Label(self.window)
        self.feed_produtos.grid(row=4, column=0, columnspan=3, sticky="nsw")
        self.feed_produtos.configure(text=" Feed Produtos", font="Times 50 bold",bg= "white", fg="gray18")
        
        #Listbox e scrollbar
        self.frame_listbox_1 = tk.Frame(self.window)
        self.frame_listbox_1.grid(row=5, rowspan = 6, column=0,columnspan=3, sticky="nswe")
        self.frame_listbox_1.rowconfigure(0, minsize=280)
        self.frame_listbox_1.rowconfigure(1, minsize=20)
        self.frame_listbox_1.columnconfigure(0, minsize=580)
        self.frame_listbox_1.columnconfigure(1, minsize=20)
        self.frame_listbox_1.configure(bg= "white")
        
        self.listbox_1 = tk.Listbox(self.frame_listbox_1)
        self.listbox_1.grid(row=0,column = 0, sticky="nwse")
        self.listbox_1.configure( font="Times 20 bold",bg= "white")
        self.listbox_1.bind("<Double-Button-1>", self.s1e3)
        
        self.scrollbar_x_1 = tk.Scrollbar(self.frame_listbox_1, orient=tk.HORIZONTAL)
        self.scrollbar_x_1.config(command=self.listbox_1.xview)
        self.scrollbar_x_1.grid(row=1, column=0, sticky="nsew")
        self.listbox_1.configure(yscrollcommand=self.scrollbar_x_1.set)
        
        self.scrollbar_y_1 = tk.Scrollbar(self.frame_listbox_1, orient=tk.VERTICAL)
        self.scrollbar_y_1.config(command=self.listbox_1.yview)
        self.scrollbar_y_1.grid(row=0, column=1, sticky="nsew")
        self.listbox_1.configure(yscrollcommand=self.scrollbar_y_1.set)
        
        #Foto2
        self.diretorio_1 = "fotoproj.jpg"
        self.img_1 = ImageTk.PhotoImage(Image.open(self.diretorio_1))
        self.imglabel_1 = tk.Label(self.window, image=self.img_1) 
        self.imglabel_1.grid(row=3, rowspan=5, column=3, columnspan=5)
#    
    def search_pagina(self):
        
        self.search = ""
        self.search_st = tk.StringVar()
        
        #Botao search
        self.botao_search = tk.Button(self.window)
        self.botao_search.grid(row=3, column=0, sticky="ew")
        self.botao_search.configure(command=self.s1_pe1_p, font="Times 25 bold", text="Pesquisar")
        
        #Entry search
        self.search_cx = tk.Entry(self.window)
        self.search_cx.grid(row=3, column=1, sticky="e")
        self.search_cx.configure(font="Times 25 bold", textvariable = self.search_st, bg="white")
        self.search_cx.bind("<Return>", self.apertou_enter_pesquisa1)
        
        #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Save & Trade", command=self.s1_pe1,font="Times 60 bold", bg="chartreuse3",fg="gray18")
        
        #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)     
        self.user_name.grid(row=0, rowspan=2, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(command=self.s1_pe2,text="Meus produtos", font="Times 30 bold", bg = "chartreuse3",fg="gray18")
        
        #Botao Logout
        self.botao_logout = tk.Button(self.window)
        self.botao_logout.grid(row=8,column=6)
        self.botao_logout.configure(text="Logout", command=self.s1_pe0,font="Times 18 bold",bg= "white")
        self.botao_logout.bind("<Return>", self.s1_pe0_enter)
        
        #Label Feed produtos
        self.pesquisar_produtos = tk.Label(self.window)
        self.pesquisar_produtos.grid(row=4, column=0, columnspan=3, sticky="nsw")
        self.pesquisar_produtos.configure(text=" Produtos Pesquisados", font="Times 45 bold",bg= "white", fg="gray18")

        #Listbox e scrollbar
        self.frame_listbox_2 = tk.Frame(self.window)
        self.frame_listbox_2.grid(row=5, rowspan = 6, column=0,columnspan=3, sticky="nswe")
        self.frame_listbox_2.rowconfigure(0, minsize=280)
        self.frame_listbox_2.rowconfigure(1, minsize=20)
        self.frame_listbox_2.columnconfigure(0, minsize=580)
        self.frame_listbox_2.columnconfigure(1, minsize=20)
        self.frame_listbox_2.configure(bg= "white")
        
        self.listbox_2 = tk.Listbox(self.frame_listbox_2)
        self.listbox_2.grid(row=0,column = 0, sticky="nwse")
        self.listbox_2.configure( font="Times 20 bold",bg= "white")
        self.listbox_2.bind("<Double-Button-1>", self.s1_pe3)
        
        self.scrollbar_x_2 = tk.Scrollbar(self.frame_listbox_2, orient=tk.HORIZONTAL)
        self.scrollbar_x_2.config(command=self.listbox_2.xview)
        self.scrollbar_x_2.grid(row=1, column=0, sticky="nsew")
        self.listbox_2.configure(yscrollcommand=self.scrollbar_x_2.set)
        
        self.scrollbar_y_2 = tk.Scrollbar(self.frame_listbox_2, orient=tk.VERTICAL)
        self.scrollbar_y_2.config(command=self.listbox_2.yview)
        self.scrollbar_y_2.grid(row=0, column=1, sticky="nsew")
        self.listbox_2.configure(yscrollcommand=self.scrollbar_y_2.set)
        
        #Foto2
        self.diretorio_1 = "fotoproj.jpg"
        self.img_1 = ImageTk.PhotoImage(Image.open(self.diretorio_1))
        self.imglabel_1 = tk.Label(self.window, image=self.img_1) 
        self.imglabel_1.grid(row=3, rowspan=5, column=3, columnspan=5)
              
    def segunda_pagina(self):
            
        #criar stringvar
        self.preco = ""
        self.preco_st = tk.StringVar()
        
        self.troca = ""
        self.troca_st = tk.StringVar()
        
        self.produto = ""
        self.produto_st = tk.StringVar()
        
        self.descricao = ""
        self.descricao_st = tk.StringVar()
                
        #Listbox e scrollbar
        
        self.frame_listbox = tk.Frame(self.window)
        self.frame_listbox.grid(row=4, rowspan = 6, column=3,columnspan=5, sticky="nsew")
        self.frame_listbox.rowconfigure(0, minsize=380)
        self.frame_listbox.rowconfigure(1, minsize=20)
        self.frame_listbox.columnconfigure(0, minsize=580)
        self.frame_listbox.columnconfigure(1, minsize=20)
        self.frame_listbox.configure(bg= "white")
        
        self.listbox = tk.Listbox(self.frame_listbox)
        self.listbox.grid(row=0,column = 0, sticky="nsew")
        self.listbox.configure( font="Times 30 bold")
        self.listbox.bind("<Double-Button-1>", self.s2e3)
        
        self.scrollbar_x = tk.Scrollbar(self.frame_listbox, orient=tk.HORIZONTAL)
        self.scrollbar_x.config(command=self.listbox.xview)
        self.scrollbar_x.grid(row=1, column=0, sticky="nsew")
        self.listbox.configure(yscrollcommand=self.scrollbar_x.set)
        
        self.scrollbar_y = tk.Scrollbar(self.frame_listbox, orient=tk.VERTICAL)
        self.scrollbar_y.config(command=self.listbox.yview)
        self.scrollbar_y.grid(row=0, column=1, sticky="nsew")
        self.listbox.configure(yscrollcommand=self.scrollbar_y.set)
        
        #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Save & Trade",command=self.s2e1, font="Times 60 bold", bg="chartreuse3", fg="gray18")
        
        #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)
        self.user_name.grid(row=0, rowspan=2, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(command=self.s2e2,text="Meus produtos", font="Times 30 bold", bg = "chartreuse3", fg="gray18")
        
        #Botao Logout
        self.botao_logout = tk.Button(self.window)
        self.botao_logout.grid(row=8,column=6)
        self.botao_logout.configure(text="Logout", command=self.s2e0,font="Times 18 bold",bg= "white")
        self.botao_logout.bind("<Return>", self.s2e0_enter)

        #Label Cadastrar Produtos
        self.cadastrar_produtos = tk.Label(self.window)
        self.cadastrar_produtos.grid(row=3, column=0, columnspan=3, sticky="nsw")
        self.cadastrar_produtos.configure(text=" Cadastrar Produtos", font="Times 30 bold",bg= "white", fg="gray18")
        
        #Label Nome produto
        self.nome_produto = tk.Label(self.window)
        self.nome_produto.grid(row=4, column=0, columnspan=3, sticky="nsw")
        self.nome_produto.configure(text=" Produto:", font="Times 20 bold",bg= "white", fg="gray18")
        
        #Entery Nome produto
        self.nome_produto_cx = tk.Entry(self.window)
        self.nome_produto_cx.grid(row=4, column=1, columnspan=3, sticky="w")
        self.nome_produto_cx.configure(font="Times 25 bold" , textvariable = self.produto_st)
        
        #Label Preco produto
        self.preco_produto = tk.Label(self.window)
        self.preco_produto.grid(row=5, column=0, columnspan=3, sticky="nsw")
        self.preco_produto.configure(text=" Preço:", font="Times 20 bold",bg= "white", fg="gray18")
        
        #Entery Preco Produto
        self.preco_produto_cx = tk.Entry(self.window)
        self.preco_produto_cx.grid(row=5, column=1, columnspan=3, sticky="w")
        self.preco_produto_cx.configure(font="Times 25 bold" , textvariable = self.preco_st)
        
        #Label Troca Produto
        self.troca_produto = tk.Label(self.window)
        self.troca_produto.grid(row=6, column=0, columnspan=3, sticky="nsw")
        self.troca_produto.configure(text=" Troca:", font="Times 20 bold",bg= "white", fg="gray18")
        
        #Entery Troca Produto
        self.troca_produto_cx = tk.Entry(self.window)
        self.troca_produto_cx.grid(row=6, column=1, columnspan=3, sticky="w")
        self.troca_produto_cx.configure(font="Times 25 bold" , textvariable = self.troca_st)
        
        #Label Meus Produtos Anunciados
        self.meus_produtos_anun = tk.Label(self.window)
        self.meus_produtos_anun.grid(row=3, column=3, columnspan=6, sticky="nsw")
        self.meus_produtos_anun.configure(text=" Meus Produtos Anunciados", font="Times 30 bold",bg= "white", fg="gray18")
        
        #Label descrição
        self.descricao_label = tk.Label(self.window)
        self.descricao_label.grid(row=7, column=0, columnspan=6, sticky="nsw")
        self.descricao_label.configure(text=" Descrição:", font="Times 20 bold",bg= "white", fg="gray18")
        
        #Entry Descrição
        self.descricao_cx = tk.Entry(self.window)
        self.descricao_cx.grid(row=7, column=1, columnspan=3, sticky="w")
        self.descricao_cx.configure(font="Times 25 bold" , textvariable = self.descricao_st)
        self.descricao_cx.bind("<Return>",self.s2e2_confirma_enter)
        
        
        #Botao confirmar
        self.botao_confirmar=tk.Button(self.window)
        self.botao_confirmar.grid(row=8, column=0)
        self.botao_confirmar.configure(text="Confirma", font="Times 20 bold",command=self.s2e2_confirma,bg= "white")
        self.botao_confirmar.bind("<Return>",self.s2e2_confirma_enter)
        
        #Label Faltaram dados
        self.faltaram_dados_p2 = tk.Label(self.window)
        self.faltaram_dados_p2.grid(row=8, column=1, columnspan=2, sticky="nswe")
        self.faltaram_dados_p2.configure(text="", font="Times 20 bold",bg= "white")
        
        
    def terceira_pagina(self):
        #Botao Slogan
        self.slogan = tk.Button(self.window)
        self.slogan.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="nsw")
        self.slogan.configure(text="Save & Trade",command=self.s3e1, font="Times 60 bold", bg="chartreuse3", fg="gray18")
        
        #Botao Nome do Usuario
        self.user_name = tk.Button(self.window)
        self.user_name.grid(row=0, rowspan=2, column=4, columnspan=6, sticky="nse")
        self.user_name.configure(command=self.s3e2,text="Meus produtos", font="Times 30 bold", bg = "chartreuse3", fg="gray18")
        
        #Botao Logout
        self.botao_logout = tk.Button(self.window)
        self.botao_logout.grid(row=8,column=6)
        self.botao_logout.configure(text="Logout", command=self.s3e0,font="Times 18 bold",bg= "white")
        self.botao_logout.bind("<Return>", self.s3e0_enter)
        
#        #Foto3
#        self.diretorio_3 = "fechou.jpg"
#        self.img_3 = ImageTk.PhotoImage(Image.open(self.diretorio_3))
#        self.imglabel_3= tk.Label(self.window, image=self.img_3) 
#        self.imglabel_3.grid(row=4, rowspan=4, column=0, columnspan=2)
        
        #Label Descrição Produto
        self.descricao_produto = tk.Label(self.window, anchor='w',wraplength=700, justify='left')
        self.descricao_produto.grid(row=4, column=3, columnspan=6, sticky="nsw")
        self.descricao_produto.configure(font="Times 25 bold",bg= "white", fg="gray18")
        
        #Label Preco Troca Produto
        self.info_preco_produto = tk.Label(self.window)
        self.info_preco_produto.grid(row=5, column=3, columnspan=6, sticky="nsw")
        self.info_preco_produto.configure( font="Times 25 bold",bg= "white", fg="gray18")
        
        #Label Email
        self.info_email_produto = tk.Label(self.window)
        self.info_email_produto.grid(row=6, column=3, columnspan=6, sticky="nsw")
        self.info_email_produto.configure( font="Times 25 bold",bg= "white", fg="gray18")
        
        #Label Descricao
        self.info_descricao =  tk.Label(self.window, anchor='w',wraplength=700, justify='left')
        self.info_descricao.grid(row=7, column=3, columnspan=6, sticky="nesw")
        self.info_descricao.configure( font="Times 20 bold",bg= "white", fg="gray18")
        
    def iniciar(self):
        self.window.mainloop()
        
    def nome_st (self):
        self.user_log = self.user_log_st.get()
        self.senha_log = self.senha_log_st.get()
        self.user_cad = self.user_cad_st.get()
        self.senha_cad = self.senha_cad_st.get()
        self.email = self.email_st.get()
    
    #Cadastramento do produto
    def cadastro_produto_st(self):
        self.produto = self.produto_st.get()
        self.preco = self.preco_st.get()
        self.troca = self.troca_st.get()
        self.descricao = self.descricao_st.get()
    
    def pesquisa_st(self):
        self.search = self.search_st.get()
    
    def search_play(self):
        self.lista_basica = []
        self.pesquisa_st()
        if self.search != "":
            self.t_prod_u = self.fb.get("/todos_os_produtos/geral","top")
            v = self.search[0].upper()+self.search[1:]
            v1 = self.search.lower()
            for i in self.t_prod_u:
                if v in i:
                    self.lista_basica.append(i)
                if v1 in i:
                    self.lista_basica.append(i)
            self.limpar_1()
            self.search_pagina()
            for i in range(len(self.lista_basica)):
                self.listbox_2.insert(tk.END, self.lista_basica[i])
                
    def cadastro_existente(self):
        self.limpar_1()
        self.pagina_0()
        self.login_fail.configure(text="Usuário existente",font = "Times 18 bold",fg="red", bg= "white")
            
    #Criando as funções de callback
    def cadastro_geral(self):
        if self.user_cad != "":
            self.fb.put("user",self.user_cad,{"senha":self.senha_cad,"email":self.email})
        
    def verificar(self):
        self.u_log = self.fb.get("/user",self.user_log)
        if self.u_log != None:
            if self.u_log["senha"]==self.senha_log:
                return True
        return False
        
    def cadastro_vazio(self):
        self.limpar_1()
        self.pagina_0()
        self.login_fail.configure(text="Faltaram dados",font = "Times 18 bold",fg="red", bg= "white")
    
    def login_incorreto(self):
        self.limpar_1()
        self.pagina_0()
        self.login_fail1.configure(text="                   Login incorreto",font = "Times 12 bold",fg="red", bg= "chartreuse3")
    
    def limpar_0(self):
        self.slogan.grid_forget()
        self.login_fail1.configure(text="")
        self.login_fail.configure(text="")
        self.login.grid_forget()
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
        self.imglabel.grid_forget()
        
        self.nome_st()
#        self.cadastro_geral()
        
        #Botao excluir
        self.botao_excluir = tk.Button(self.window)
        self.botao_excluir .grid(row=8,column=5)
        self.botao_excluir.configure(text="Excluir", command=self.s3e2_excluir,font="Times 18 bold",bg= "white")
        self.botao_excluir.grid_forget()
        
        #lista de todos os produtos de um usuário
        if self.user_log != "":
            LU = self.fb.get("/user/{0}".format(self.user_log),"todos_produtos")
            if LU == None:
                self.lista_prod_tot = []
            else:
                self.lista_prod_tot = LU
        
    def limpar_1(self):
        self.botao_search.grid_forget()
        self.search_cx.grid_forget()
        self.slogan.grid_forget()
        self.user_name.grid_forget()
        self.feed_produtos.grid_forget()
        self.frame_listbox_1.grid_forget()
        self.listbox_1.grid_forget()
        self.scrollbar_x_1.grid_forget()
        self.scrollbar_y_1.grid_forget()
        self.botao_logout.grid_forget()
        self.imglabel_1.grid_forget()        
    
    def limpar_1_search(self):
        self.botao_search.grid_forget()
        self.search_cx.grid_forget()
        self.slogan.grid_forget()
        self.user_name.grid_forget()
        self.pesquisar_produtos.grid_forget()
        self.frame_listbox_2.grid_forget()
        self.listbox_2.grid_forget()
        self.scrollbar_x_2.grid_forget()
        self.scrollbar_y_2.grid_forget()
        self.botao_logout.grid_forget()
        self.imglabel_1.grid_forget()
        
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
        self.frame_listbox.grid_forget()
        self.listbox.grid_forget()
        self.scrollbar_x.grid_forget()
        self.scrollbar_y.grid_forget()
        self.botao_confirmar.grid_forget()
        self.botao_logout.grid_forget()
        self.descricao_label.grid_forget()
        self.descricao_cx.grid_forget()
        self.faltaram_dados_p2.configure(text="", font="Times 20 bold",bg= "white", fg="gray18")
        
    def limpar_3(self):
        if self.p == 1 or self.p==2:
            self.botao_email.grid_forget()
        self.slogan.grid_forget()
        self.user_name.grid_forget()
        self.descricao_produto.grid_forget()
        self.info_preco_produto.grid_forget()
        self.info_email_produto.grid_forget()
        self.botao_logout.grid_forget()
        self.botao_excluir.grid_forget() 
        self.info_descricao.grid_forget()
       # self.imglabel_3.grid_forget()
        
           
   
    def pagina_0(self):
        self.zero_pagina()
        
    def pagina_1(self):
       self.primeira_pagina()
        
    def pagina_2(self):
        self.segunda_pagina()
        
    def pagina_3(self):
        self.terceira_pagina()

    def botao_user_log(self):
        if self.user_log != "":
            if self.senha_log != "":
                if self.verificar() == True:
                    self.A = 0
                    return self.A
                else:
                    self.login_incorreto()
            else:
                self.login_incorreto()
        elif self.user_log == "":
            self.login_incorreto()
            
    def botao_user_cad(self):
        if self.user_cad != "" and self.senha_cad !="" and self.email !="":
            if self.fb.get("/user",self.user_cad) != None:
                self.cadastro_existente()
            else:
                self.A = 1
                return self.A
        elif self.user_cad == "" or self.senha_cad == "" or self.email== "":
            self.cadastro_vazio()
            


    def s1_pe0(self):
        self.limpar_1_search()
        self.pagina_0()
            
            
    def s0e1_log(self):
        self.lista_prod_tot = []
        self.limpar_0()
        self.pagina_1()
        self.botao_user_log()
        self.entra_listbox_feed()
        
    def s0e1_cad(self):
        self.lista_prod_tot = []
        self.limpar_0()
        self.pagina_1()
        self.botao_user_cad()
        if self.A == 1:
            self.cadastro_geral()
        self.entra_listbox_feed()
    
    def s1e1(self):
        self.limpar_1()
        self.pagina_1()
        self.entra_listbox_feed()
        
    def s1_pe1(self):
        self.limpar_1_search()
        self.pagina_1()
        self.entra_listbox_feed()
    
    
    def s1_pe1_p(self):
        self.limpar_1_search()
        self.search_play()
    
    def s1e2(self):
        self.limpar_1()
        self.pagina_2()
        self.entra_listbox()
        
    def s1_pe2(self):
        self.limpar_1_search()
        self.pagina_2()
        self.entra_listbox()
                
    def s1e3(self,event):
        self.limpar_1()
        self.pagina_3()
        self.listbox_1.curselection()
        self.achar_produto_s1e3()
        self.p = 2
        
        #Botao email
        self.botao_email = tk.Button(self.window)
        self.botao_email.grid(row=8,column=5)
        self.botao_email.configure(text="E-mail", command=self.enviar_email,font="Times 18 bold",bg= "white")
    
    def s1_pe3(self,event):
        self.limpar_1_search()
        self.pagina_3()
        self.listbox_2.curselection()
        self.achar_produto_s1_pe3()
        self.p = 1
        
        #Botao email
        self.botao_email = tk.Button(self.window)
        self.botao_email.grid(row=8,column=5)
        self.botao_email.configure(text="E-mail", command=self.enviar_email,font="Times 18 bold",bg= "white")
        
    def s2e1(self):
        self.limpar_2()
        self.pagina_1()
        self.entra_listbox_feed()
    
    def s2e2_confirma(self):
        self.cadastro_produto_st()
        if self.produto != "":
            if self.preco == "" and self.troca == "":
                 self.faltaram_dados_p2.configure(text="Faltaram dados", font="Times 20 bold",bg= "white", fg="red")
                 print("Caue")
            else:
                
                self.cadastro_produto_st()
                self.lista_prod_tot.append(self.produto)
                self.t_prod_u.append(self.produto)
                self.produto_user = self.fb.get("/produto",self.produto)
                if self.user_cad != "":
                    if self.preco != "" or self.troca != "":
                        if self.produto_user == None:
                            self.fb.put("/produto",self.produto,{"nome":self.user_cad})
                            self.lista_prod_tot_at = self.fb.patch("/user/{0}".format(self.user_cad),{"todos_produtos":self.lista_prod_tot})
                            self.u_prod = self.fb.patch("/user/{0}".format(self.user_cad),{self.produto:{"preço":self.preco,"troca":self.troca,"descrição":self.descricao}})
                            self.prod_usu = self.fb.patch("/todos_os_produtos/geral",{"top":self.t_prod_u})
    
                        else:
                            toplevel1 = tk.Toplevel(self.window)
                            label = tk.Label(toplevel1, text="Já existe um produto com esse nome!", font="Times 20 bold", fg="red", height=0, width=30)
                            label.pack()
                elif self.user_log != "":
                    if self.preco != "" or self.troca != "":
                        if self.produto_user == None:
                            self.fb.put("/produto",self.produto,{"nome":self.user_log})
                            self.lista_prod_tot_at = self.fb.patch("/user/{0}".format(self.user_log),{"todos_produtos":self.lista_prod_tot})
                            self.u_prod = self.fb.patch("/user/{0}".format(self.user_log),{self.produto:{"preço":self.preco,"troca":self.troca,"descrição":self.descricao}})
                            self.prod_usu = self.fb.patch("/todos_os_produtos/geral",{"top":self.t_prod_u})
                        else:
                            toplevel1 = tk.Toplevel(self.window)
                            label = tk.Label(toplevel1, text="Já existe um produto com esse nome!", font="Times 20 bold", fg="red", height=0, width=30)
                            label.pack()        
                            
                self.limpar_2()
                self.pagina_2()
                self.entra_listbox_feed()
                self.entra_listbox()
            
        
        
    def s2e2(self):
        self.limpar_2()
        self.pagina_2()
        self.entra_listbox()
        
    def s2e3(self,event):
        self.limpar_2()
        self.pagina_3()
        self.achar_produto_s2e3() 
        
        #Botao excluir
        self.botao_excluir = tk.Button(self.window)
        self.botao_excluir .grid(row=8,column=5)
        self.botao_excluir.configure(text="Excluir", command=self.s3e2_excluir,font="Times 18 bold",bg= "white")
        
    def s3e1(self):
        self.limpar_3()
        self.pagina_1()
        self.entra_listbox_feed()
        
    def s3e2(self):
        self.limpar_3()
        self.pagina_2()
        self.entra_listbox()
    
    def s3e2_excluir(self):
        if self.user_log != "":
            self.fb.delete("/user/{0}".format(self.user_log),self.nome_excluir)
            self.lista_prod_tot = self.fb.get("/user/{0}".format(self.user_log),"todos_produtos")
            self.fb.delete("/user/{0}".format(self.user_log),"todos_produtos")
            v = self.lista_prod_tot[self.listbox.curselection()[0]]
            del self.lista_prod_tot[self.listbox.curselection()[0]]
            self.fb.patch("/user/{0}".format(self.user_log),{"todos_produtos":self.lista_prod_tot})
        if self.user_cad != "":
            self.fb.delete("/user/{0}".format(self.user_cad),self.nome_excluir)
            self.lista_prod_tot = self.fb.get("/user/{0}".format(self.user_cad),"todos_produtos")
            self.fb.delete("/user/{0}".format(self.user_cad),"todos_produtos")
            v = self.lista_prod_tot[self.listbox.curselection()[0]]
            del self.lista_prod_tot[self.listbox.curselection()[0]]
            self.fb.patch("/user/{0}".format(self.user_cad),{"todos_produtos":self.lista_prod_tot})
        self.t_prod_u = self.fb.get("/todos_os_produtos/geral","top")
        self.fb.delete("/todos_os_produtos/geral","top")
        self.t_prod_u.remove(v)
        self.fb.patch("/todos_os_produtos/geral",{"top":self.t_prod_u})
        self.limpar_3()
        self.pagina_2()
        self.entra_listbox()
        
    def s1e0(self):
        self.limpar_1()
        self.pagina_0()
        
    def s2e0(self):
        self.limpar_2()
        self.pagina_0()
        
    def s3e0(self):
        self.limpar_3()
        self.pagina_0()
        
    def entra_listbox (self):
        if self.lista_prod_tot != []:
            if self.user_log != "":
                self.prod_total = self.fb.get("/user/{0}".format(self.user_log),self.produto)
                self.prod_preco = self.fb.get("/user/{0}/{1}".format(self.user_log,self.produto),"preço")
                self.prod_troca = self.fb.get("/user/{0}/{1}".format(self.user_log,self.produto),"troca")
                self.lista_prod_tot = self.fb.get("/user/{0}".format(self.user_log),"todos_produtos")
                if self.lista_prod_tot != []:
                    for i in range(len(self.lista_prod_tot)):
                        self.listbox.insert(tk.END, self.lista_prod_tot[i])
                        
            elif self.user_cad != "":
                self.prod_total = self.fb.get("/user/{0}".format(self.user_cad),self.produto)
                self.prod_preco = self.fb.get("/user/{0}/{1}".format(self.user_cad,self.produto),"preço")
                self.prod_troca = self.fb.get("/user/{0}/{1}".format(self.user_cad,self.produto),"troca")
                self.lista_prod_tot = self.fb.get("/user/{0}".format(self.user_cad),"todos_produtos")
                if self.lista_prod_tot != []:
                    for i in range(len(self.lista_prod_tot)):
                        self.listbox.insert(tk.END, self.lista_prod_tot[i])
                        
    def entra_listbox_feed(self):
        self.prod_usu = self.fb.get("/todos_os_produtos/geral","top")
        if self.t_prod_u != []:
            for i in range(len(self.prod_usu)):
                self.listbox_1.insert(tk.END, self.prod_usu[i])
            
    def achar_produto_s2e3 (self):
        if self.user_log != "":
            self.u_log_email = self.fb.get("/user/{0}".format(self.user_log),"email")
            self.prod_total = self.fb.get("/user/{0}".format(self.user_log),self.lista_prod_tot[self.listbox.curselection()[0]])
            self.lista_prod_tot = self.fb.get("/user/{0}".format(self.user_log),"todos_produtos")
            self.nome_excluir = self.lista_prod_tot[self.listbox.curselection()[0]]
            self.descricao_produto.configure (text = "Produto: {0}".format(self.lista_prod_tot[self.listbox.curselection()[0]]))
            self.info_preco_produto.configure(text="Preço: {0} \n \n Troca: {1}" .format(self.prod_total["preço"],self.prod_total["troca"]))
            self.info_email_produto.configure(text="E-mail: {0}".format(self.u_log_email))
        elif self.user_cad != "":
            self.u_cad_email = self.fb.get("/user/{0}".format(self.user_cad),"email")
            self.prod_total = self.fb.get("/user/{0}".format(self.user_cad),self.lista_prod_tot[self.listbox.curselection()[0]])
            self.lista_prod_tot = self.fb.get("/user/{0}".format(self.user_cad),"todos_produtos")
            self.nome_excluir = self.lista_prod_tot[self.listbox.curselection()[0]]
            self.descricao_produto.configure (text = "Produto: {0}".format(self.lista_prod_tot[self.listbox.curselection()[0]]))
            self.info_preco_produto.configure(text="Preço: {0} \n \n Troca: {1}" .format(self.prod_total["preço"],self.prod_total["troca"]))
            self.info_email_produto.configure(text="E-mail: {0}".format(self.u_cad_email))
        self.info_descricao.configure(text="Descrição: {0}".format(self.prod_total["descrição"]))
        
    def achar_produto_s1e3 (self):
        
        self.nome_excluir = self.t_prod_u[self.listbox_1.curselection()[0]]
        self.vendedor = self.fb.get("/produto/{0}".format(self.nome_excluir),"nome")
        self.preco_fb = self.fb.get("/user/{0}/{1}".format(self.vendedor,self.nome_excluir),"preço")
        self.troca_fb = self.fb.get("/user/{0}/{1}".format(self.vendedor,self.nome_excluir),"troca")
        self.descricao_fb = self.fb.get("/user/{0}/{1}".format(self.vendedor,self.nome_excluir),"descrição")
        self.email_fb = self.fb.get("/user/{0}".format(self.vendedor),"email")
        self.descricao_produto.configure (text = "Produto: {0}".format(self.t_prod_u[self.listbox_1.curselection()[0]]))
        self.info_preco_produto.configure(text="Preço: {0} \n \n Troca: {1} ".format(self.preco_fb,self.troca_fb))
        self.info_email_produto.configure(text="E-mail: {0}".format(self.email_fb))
        self.info_descricao.configure(text="Descrição: {0}".format(self.descricao_fb))
    
    def achar_produto_s1_pe3 (self):
        
        self.nome_excluir = self.lista_basica[self.listbox_2.curselection()[0]]
        self.vendedor = self.fb.get("/produto/{0}".format(self.nome_excluir),"nome")
        self.preco_fb = self.fb.get("/user/{0}/{1}".format(self.vendedor,self.lista_basica[self.listbox_2.curselection()[0]]),"preço")
        self.troca_fb = self.fb.get("/user/{0}/{1}".format(self.vendedor,self.lista_basica[self.listbox_2.curselection()[0]]),"troca")
        self.descricao_fb = self.fb.get("/user/{0}/{1}".format(self.vendedor,self.lista_basica[self.listbox_2.curselection()[0]]),"descrição")
        self.email_fb = self.fb.get("/user/{0}".format(self.vendedor),"email")
        self.descricao_produto.configure (text = "Produto: {0}".format(self.lista_basica[self.listbox_2.curselection()[0]]))
        self.info_preco_produto.configure(text="Preço: {0} \n \n Troca: {1} ".format(self.preco_fb,self.troca_fb))
        self.info_email_produto.configure(text="E-mail: {0}".format(self.email_fb))
        self.info_descricao.configure(text="Descrição: {0}".format(self.descricao_fb))   
        
    def enviar_email(self):
        if self.p == 1:
            self.nome_excluir = self.t_prod_u[self.listbox_2.curselection()[0]]
            self.vendedor = self.fb.get("/produto/{0}".format(self.nome_excluir),"nome")
            self.email_fb = self.fb.get("/user/{0}".format(self.vendedor),"email")
            if self.user_cad != "":
                email = self.fb.get("/user/{0}".format(self.user_cad),"email")
                content = ("O user {0} tem interesse no seu produto {1}. O email do interessado: {2}.".format(self.user_cad,self.lista_basica[self.listbox_2.curselection()[0]],email)).encode("UTF-8")
            elif self.user_log != "":
                email = self.fb.get("/user/{0}".format(self.user_log),"email")
                content = ("O user {0} tem interesse no seu produto {1}. O email do interessado: {2}.".format(self.user_log,self.lista_basica[self.listbox_2.curselection()[0]],email)).encode("UTF-8")
        else:
            if self.user_cad != "":
                email = self.fb.get("/user/{0}".format(self.user_cad),"email")
                content = ("O user {0} tem interesse no seu produto {1}. O email do interessado: {2}.".format(self.user_cad,self.t_prod_u[self.listbox_1.curselection()[0]],email)).encode("UTF-8")
            elif self.user_log != "":
                email = self.fb.get("/user/{0}".format(self.user_log),"email")
                content = ("O user {0} tem interesse no seu produto {1}. O email do interessado: {2}.".format(self.user_log,self.t_prod_u[self.listbox_1.curselection()[0]],email)).encode("UTF-8")
#        v_email = validate_email(self.email_fb.get())
        subject = "Troca e Venda:"
        message = "Subject: {0}\n\n{1}".format(subject,content)
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("troca.venda.2016@gmail.com","trocavenda")
        mail.sendmail("troca.venda.2016@gmail.com",self.email_fb,message)
        mail.close()
        
        self.s3e1()
        
        toplevel = tk.Toplevel(self.window)
        label = tk.Label(toplevel, text="Email enviado!", font="Times 25 bold", fg="blue", height=0, width=20)
        label.pack()


    def s0e1_log_enter(self,event):
        self.s0e1_log()
        
    def s0e1_cad_enter(self,event):
        self.s0e1_cad()
        
    def apertou_enter_pesquisa(self, event):
        self.search_play()
        
    def apertou_enter_pesquisa1(self, event):
        self.s1_pe1_p()
    
    def s1e0_enter(self, event):
        self.s1e0()
        
    def s1_pe0_enter(self, event):
        self.s1_pe0()
        
    def s2e0_enter(self, event):
        self.s2e0()
    
    def s3e0_enter(self, event):
        self.s3e0()
        
    def s2e2_confirma_enter(self,event):
        self.s2e2_confirma()

Site = Tela_Login()

Site.iniciar()   
