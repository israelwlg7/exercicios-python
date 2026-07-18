import customtkinter as ctk
import time
ctk.set_appearance_mode("dark") # dark, system, light
ctk.set_default_color_theme("blue") # blue, green, dark-blue



class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        # executa os meus codigos personalizados
        self.title("Sistema de Cadastro de Clientes")
        self.geometry("900x600")
        
        # criar divisão da tela weight = 1 -> expande junto com a tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=200) #você pode utilizar dentro do parentese o parametro sticky esse paremetro ele define com vc falando tipo pra onde você quer a borda expanda stick=n ele vai expandir pra cima porque ta pro norte
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")#aqui você ta adicionando eles e informando em que parte a aba lateral vai ficar, não pode esquecer de passar o self dentro pra ele fazer parte da janela principal

        # parte principal
        self.janela_abas = ctk.CTkTabview(self, width=400) # e você utilizando o padyx ele da uma separada entre uma barra e a outra uma divisão de 10 pixels
        self.janela_abas.grid(row=0, column=1, sticky="nsew", padx=10) # você ainda pode usar o pack mais utilizando o grid ele te da mais livre arbitrio digamos vc pode passar aonde quer colocar ja o pack ele vai indo pra baixo

        self.janela_abas.add("Perfil")
        self.janela_abas.add("Preferências")
        self.janela_abas.add("Dashboard")
        # preencher as partes/abas

        # preencher aba lateral
        self.construir_abalateral()
        # preencher aba do perfil
        self.construir_abaperfil()
        # preenncher aba preferências
        self.construir_abapreferencias()
        # preencher aba sistema
        self.construir_abasistema()

        

    def construir_abalateral(self):
        self.titulo = ctk.CTkLabel(self.barra_lateral,
                                   text="Meu App",
                                   font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=(30, 10), padx=(20, 20))
        self.subtitulo = ctk.CTkLabel(self.barra_lateral,
                                   text="")
        self.subtitulo.pack(pady=(0, 5))
        self.botao_principal = ctk.CTkButton(self.barra_lateral,
                                             text="Dashbord Principal",
                                             command=self.ir_para_dashboard)
        self.botao_principal.pack(pady=(30,30), padx=(10, 10))

        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral, 
                                             text="Modo Escuro",
                                             command=self.mudar_modo_dark)
        self.switch_mododark.pack(pady=(10,10), side="bottom")
        self.switch_mododark.select()
        
    def construir_abaperfil(self):

        self.aba_perfil = self.janela_abas.tab("Perfil")
        #campo de nome
        self.campo_nome = ctk.CTkEntry(self.aba_perfil,
                                  placeholder_text="Digite o seu nome",
                                  width=300)
        self.campo_nome.pack(pady=(20, 20))

        # radio button do nivel de usuario
        self.nivel_usuario = ctk.IntVar(value=0)
        self.radio_label = ctk.CTkLabel(self.aba_perfil, text="Nível usuário")
        self.radio_basico = ctk.CTkRadioButton(self.aba_perfil,
                                               text="Básico",
                                               variable=self.nivel_usuario,
                                               value=1)
        self.radio_admin = ctk.CTkRadioButton(self.aba_perfil,text="Admin",
                                               variable=self.nivel_usuario,
                                               value=2)
        self.radio_label.pack()
        self.radio_basico.pack()
        self.radio_admin.pack()

        # checkbox de notificações
        self.checkbox_notificacoes = ctk.CTkCheckBox(self.aba_perfil,
                                                     text="Receber Notificações por Email")
        self.checkbox_notificacoes.pack(pady=(20, 20))
        
        #botao salvar perfil
        self.botao_salvarperfil = ctk.CTkButton(self.aba_perfil,
                                             text="Salvar Perfil",
                                             fg_color="green",
                                             hover_color="darkgreen",
                                             command=self.salvar_perfil)
        self.botao_salvarperfil.pack(pady=(20, 20))

    def construir_abapreferencias(self):
        self.aba_preferencias = self.janela_abas.tab("Preferências")

        self.label_idiomas = ctk.CTkLabel(self.aba_preferencias,
                                          text="Selecione o idioma")
        self.label_idiomas.pack(pady=(20, 5))

        self.menu_idiomas = ctk.CTkOptionMenu(self.aba_preferencias,
                                              values=["português", "inglês", "Espanhol"])
        self.menu_idiomas.pack()
        
        self.label_volume = ctk.CTkLabel(self.aba_preferencias,
                                         text="Volume do Sistema")
        self.slider_volume = ctk.CTkSlider(self.aba_preferencias,
                                           from_=0,to=100,
                                           command=self.atualizar_volume)
        self.label_volume.pack(pady=(30,5))
        self.slider_volume.pack()
        self.slider_volume.set(50)

        self.label_valor_volume = ctk.CTkLabel(self.aba_preferencias,
                                               text="50%")
        self.label_valor_volume.pack()
        # slider

    def construir_abasistema(self): # aba dashbord/sistema
        self.aba_sistema = self.janela_abas.tab("Dashboard")

        self.label_carregamento = ctk.CTkLabel(self.aba_sistema,
                                               text="Testa Carregamento do Sistema",
                                               font=ctk.CTkFont(size=16))
        self.label_carregamento.pack(pady=(30, 30))

        self.barra_progresso = ctk.CTkProgressBar(self.aba_sistema,
                                                  width=400)
        self.barra_progresso.pack(pady=(10,10))
        self.barra_progresso.set(0)

        self.botao_progresso = ctk.CTkButton(self.aba_sistema,
                                             text="Iniciar Carregamento",
                                             command=self.carregar)
        self.botao_progresso.pack(pady=(20, 20))
    
    def ir_para_dashboard(self):
        self.janela_abas.set("Dashboard")

    def mudar_modo_dark(self):
        if self.switch_mododark.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def salvar_perfil(self):
        nome = self.campo_nome.get()
        if self.nivel_usuario.get() == 2:
            nivel = "Admin"
        else:
            nivel = "Básico"
        receber_notificacoes = self.checkbox_notificacoes.get()
        print("Nome", nome)
        print("nivel", nivel)
        print("Receber Notificações", receber_notificacoes)
        self.titulo.configure(text=f"{nome} App")
        self.subtitulo.configure(text=nivel)

    def atualizar_volume(self, novo_valor_volume):
        self.label_valor_volume.configure(text=f"{int(novo_valor_volume)}%")

    def carregar(self):
        for i in range(100):
            # executar uma tarefa que pode demorar
            time.sleep(0.1)
            self.barra_progresso.set((i + 1) / 100)
            self.update()

janela = Aplicativo()
janela.mainloop()
    

