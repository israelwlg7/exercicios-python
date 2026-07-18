import customtkinter as ctk
from PIL import Image
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

usuarios_cadastrados = []


class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor


class TelaInicial(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Estacionamento")
        self.geometry("900x600")
        self.resizable(False, False)

        self.fundo = ctk.CTkImage(light_image=Image.open("chat.png"),
                                  dark_image=Image.open("chat.png"),
                                  size=(900, 600))

        self.label_fundo = ctk.CTkLabel(self, image=self.fundo, text="")
        self.label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(self,width=360,
                                  height=420,
                                  corner_radius=20,
                                  fg_color=("#0F172A", 
                                            "#0F172A"))

        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)

        self.logo = ctk.CTkLabel(self.frame,
                                 text="🅿",
                                 font=ctk.CTkFont(size=55))
        self.logo.pack(pady=(25, 5))

        self.label_titulo = ctk.CTkLabel(self.frame,
                                         text="Bem-vindo!",
                                         font=ctk.CTkFont(size=30,
                                                        weight="bold"))
        self.label_titulo.pack()

        self.label_subtitulo = ctk.CTkLabel(self.frame,
                                            text="Sistema de Estacionamento",
                                            font=ctk.CTkFont(size=16))
        self.label_subtitulo.pack(pady=(5, 35))

        self.botao_login = ctk.CTkButton(self.frame,
                                         text="Fazer Login",
                                         width=280,
                                         height=45,
                                         corner_radius=12,
                                         command=self.abrir_login)
        self.botao_login.pack(pady=10)

        self.botao_cadastro = ctk.CTkButton(self.frame,
                                            text="Criar Conta",
                                            width=280,
                                            height=45,
                                            corner_radius=12,
                                            fg_color="#16A34A",
                                            hover_color="#15803D",
                                            command=self.abrir_cadastro)
        self.botao_cadastro.pack(pady=10)

        self.botao_visitante = ctk.CTkButton(self.frame,
                                             text="Entrar como Visitante",
                                             width=280,
                                             height=45,
                                             corner_radius=12,
                                             fg_color="#4B5563",
                                             hover_color="#374151",
                                             command=self.entrar_visitante)
        self.botao_visitante.pack(pady=10)

    def abrir_login(self):
        self.destroy()
        tela = TelaLogin()
        tela.mainloop()

    def abrir_cadastro(self):
        self.destroy()
        tela = TelaCadastro()
        tela.mainloop()

    def entrar_visitante(self):
        self.destroy()
        app = Aplicativo("Visitante")
        app.mainloop()

class TelaCadastro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cadastro - Sistema de Estacionamento")
        self.geometry("400x450")

        self.label_titulo = ctk.CTkLabel(self,
                                         text="Criar Conta",
                                         font=ctk.CTkFont(size=24, weight="bold"))
        self.label_titulo.pack(pady=(30, 20))

        self.label_usuario = ctk.CTkLabel(self, text="Usuário")
        self.label_usuario.pack(pady=(10, 0))

        self.campo_usuario = ctk.CTkEntry(self,
                                          placeholder_text="Escolha um nome de usuário",
                                          width=250)
        self.campo_usuario.pack(pady=(5, 10))

        self.label_senha = ctk.CTkLabel(self, text="Senha")
        self.label_senha.pack(pady=(10, 0))

        self.campo_senha = ctk.CTkEntry(self,
                                        placeholder_text="Escolha uma senha",
                                        show="*",
                                        width=250)
        self.campo_senha.pack(pady=(5, 10))

        self.label_confirmar = ctk.CTkLabel(self, text="Confirmar Senha")
        self.label_confirmar.pack(pady=(10, 0))

        self.campo_confirmar = ctk.CTkEntry(self,
                                            placeholder_text="Digite a senha novamente",
                                            show="*",
                                            width=250)
        self.campo_confirmar.pack(pady=(5, 10))

        self.botao_cadastrar = ctk.CTkButton(self,
                                             text="Cadastrar",
                                             width=250,
                                             fg_color="green",
                                             hover_color="darkgreen",
                                             command=self.fazer_cadastro)
        self.botao_cadastrar.pack(pady=(20, 10))

        self.resultado = ctk.CTkLabel(self, text="")
        self.resultado.pack(pady=5)

        self.botao_voltar = ctk.CTkButton(self,
                                          text="Voltar",
                                          width=250,
                                          fg_color="gray",
                                          hover_color="darkgray",
                                          command=self.voltar)
        self.botao_voltar.pack(pady=5)

    def fazer_cadastro(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        confirmar = self.campo_confirmar.get()

        if not usuario or not senha or not confirmar:
            self.resultado.configure(text="Preencha todos os campos!",
                                     text_color="red")
            return

        if senha != confirmar:
            self.resultado.configure(text="As senhas não coincidem!",
                                     text_color="red")
            return

        for u in usuarios_cadastrados:
            if u["usuario"] == usuario:
                self.resultado.configure(text="Usuário já existe!",
                                         text_color="red")
                return

        usuarios_cadastrados.append({"usuario": usuario, "senha": senha})
        self.resultado.configure(text="Conta criada com sucesso!",
                                 text_color="green")
        self.after(1500, self.voltar)

    def voltar(self):
        self.destroy()
        tela = TelaInicial()
        tela.mainloop()


class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login - Sistema de Estacionamento")
        self.geometry("400x400")

        self.label_titulo = ctk.CTkLabel(self,
                                         text="Login",
                                         font=ctk.CTkFont(size=24, weight="bold"))
        self.label_titulo.pack(pady=(30, 20))

        self.label_usuario = ctk.CTkLabel(self, text="Usuário")
        self.label_usuario.pack(pady=(10, 0))

        self.campo_usuario = ctk.CTkEntry(self,
                                          placeholder_text="Digite o seu usuário",
                                          width=250)
        self.campo_usuario.pack(pady=(5, 10))

        self.label_senha = ctk.CTkLabel(self, text="Senha")
        self.label_senha.pack(pady=(10, 0))

        self.campo_senha = ctk.CTkEntry(self,
                                        placeholder_text="Digite a sua senha",
                                        show="*",
                                        width=250)
        self.campo_senha.pack(pady=(5, 10))

        self.botao_login = ctk.CTkButton(self,
                                         text="Entrar",
                                         width=250,
                                         command=self.validar_login)
        self.botao_login.pack(pady=(20, 10))

        self.resultado = ctk.CTkLabel(self, text="")
        self.resultado.pack(pady=5)

        self.botao_voltar = ctk.CTkButton(self,
                                          text="Voltar",
                                          width=250,
                                          fg_color="gray",
                                          hover_color="darkgray",
                                          command=self.voltar)
        self.botao_voltar.pack(pady=5)

    def validar_login(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()

        for u in usuarios_cadastrados:
            if u["usuario"] == usuario and u["senha"] == senha:
                self.resultado.configure(text="Login feito com sucesso!",
                                         text_color="green")
                self.after(1000, self.abrir_aplicativo, usuario)
                return

        self.resultado.configure(text="Usuário ou senha incorretos!",
                                 text_color="red")

    def abrir_aplicativo(self, usuario):
        self.destroy()
        app = Aplicativo(usuario)
        app.mainloop()

    def voltar(self):
        self.destroy()
        tela = TelaInicial()
        tela.mainloop()


class Aplicativo(ctk.CTk):
    def __init__(self, usuario):
        super().__init__()

        self.usuario = usuario

        self.title("Sistema de Estacionamento")
        self.geometry("900x600")

        self.veiculos = []
        self.estacionados = []

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        self.abas = ctk.CTkTabview(self, width=400)
        self.abas.grid(row=0, column=1, sticky="nsew", padx=10)

        self.abas.add("Cadastro")
        self.abas.add("Estacionamento")
        self.abas.add("Sistema")

        self.criar_lateral()
        self.criar_cadastro()
        self.criar_estacionamento()
        self.criar_sistema()

    def criar_lateral(self):
        self.titulo = ctk.CTkLabel(self.barra_lateral,
                                   text="Meu App",
                                   font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=(30, 10), padx=(20, 20))

        self.subtitulo = ctk.CTkLabel(self.barra_lateral,
                                      text=f"Usuário: {self.usuario}")
        self.subtitulo.pack(pady=(0, 5))

        self.botao_principal = ctk.CTkButton(self.barra_lateral,
                                             text="Sistema Principal",
                                             command=self.ir_para_sistema)
        self.botao_principal.pack(pady=(30, 30), padx=(10, 10))

        self.botao_sair = ctk.CTkButton(self.barra_lateral,
                                        text="Sair",
                                        fg_color="red",
                                        hover_color="darkred",
                                        command=self.fazer_logout)
        self.botao_sair.pack(pady=(10, 10), padx=(10, 10))

        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral,
                                             text="Modo Escuro",
                                             command=self.mudar_modo_dark)
        self.switch_mododark.pack(pady=(10, 10), side="bottom")
        self.switch_mododark.select()

    def criar_cadastro(self):
        aba = self.abas.tab("Cadastro")

        self.label_cadastro_titulo = ctk.CTkLabel(aba,
                                                  text="Cadastro de Veículos",
                                                  font=ctk.CTkFont(size=16))
        self.label_cadastro_titulo.pack(pady=(20, 10))

        self.entry_placa = ctk.CTkEntry(aba,
                                        placeholder_text="Placa do veículo",
                                        width=300)
        self.entry_placa.pack(pady=10)

        self.entry_modelo = ctk.CTkEntry(aba,
                                         placeholder_text="Modelo do veículo",
                                         width=300)
        self.entry_modelo.pack(pady=10)

        self.entry_cor = ctk.CTkEntry(aba,
                                      placeholder_text="Cor do veículo",
                                      width=300)
        self.entry_cor.pack(pady=10)

        self.botao_cadastrar = ctk.CTkButton(aba,
                                             text="Cadastrar Veículo",
                                             fg_color="green",
                                             hover_color="darkgreen",
                                             command=self.cadastrar_veiculo)
        self.botao_cadastrar.pack(pady=10)

        self.resultado_cadastro = ctk.CTkLabel(aba, text="")
        self.resultado_cadastro.pack(pady=5)

        self.texto_veiculos = ctk.CTkTextbox(aba, width=500, height=200)
        self.texto_veiculos.pack(pady=10)

    def cadastrar_veiculo(self):
        placa = self.entry_placa.get()
        modelo = self.entry_modelo.get()
        cor = self.entry_cor.get()

        if placa and modelo and cor:
            veiculo = Veiculo(placa, modelo, cor)
            self.veiculos.append(veiculo)
            self.atualizar_lista_veiculos()

            self.entry_placa.delete(0, "end")
            self.entry_modelo.delete(0, "end")
            self.entry_cor.delete(0, "end")

            self.resultado_cadastro.configure(text=f"Veículo {placa} cadastrado!",
                                              text_color="green")
            self.atualizar_sistema()
        else:
            self.resultado_cadastro.configure(text="Preencha todos os campos!",
                                              text_color="red")

    def atualizar_lista_veiculos(self):
        self.texto_veiculos.delete("1.0", "end")
        for veiculo in self.veiculos:
            self.texto_veiculos.insert("end",
                                       f"{veiculo.placa} | {veiculo.modelo} | {veiculo.cor}\n")

    def criar_estacionamento(self):
        aba = self.abas.tab("Estacionamento")

        self.label_estacionamento_titulo = ctk.CTkLabel(aba,
                                                        text="Controle de Estacionamento",
                                                        font=ctk.CTkFont(size=16))
        self.label_estacionamento_titulo.pack(pady=(20, 10))

        self.entry_placa_estacionamento = ctk.CTkEntry(aba,
                                                       placeholder_text="Digite a placa do veículo",
                                                       width=300)
        self.entry_placa_estacionamento.pack(pady=10)

        self.botao_entrada = ctk.CTkButton(aba,
                                           text="Registrar Entrada",
                                           fg_color="green",
                                           hover_color="darkgreen",
                                           command=self.registrar_entrada)
        self.botao_entrada.pack(pady=5)

        self.botao_saida = ctk.CTkButton(aba,
                                         text="Registrar Saída",
                                         fg_color="red",
                                         hover_color="darkred",
                                         command=self.registrar_saida)
        self.botao_saida.pack(pady=10)

        self.resultado = ctk.CTkLabel(aba, text="")
        self.resultado.pack(pady=10)

        self.label_lista_estacionados = ctk.CTkLabel(aba,
                                                     text="Veículos no estacionamento:")
        self.label_lista_estacionados.pack(pady=(20, 5))

        self.texto_estacionados = ctk.CTkTextbox(aba, width=500, height=150)
        self.texto_estacionados.pack(pady=5)

    def registrar_entrada(self):
        placa = self.entry_placa_estacionamento.get()

        if not placa:
            self.resultado.configure(text="Digite uma placa!",
                                     text_color="red")
            return

        if placa not in self.estacionados:
            self.estacionados.append(placa)
            self.resultado.configure(text=f"{placa} entrou no estacionamento",
                                     text_color="green")
            self.atualizar_lista_estacionados()
            self.atualizar_sistema()
        else:
            self.resultado.configure(text=f"{placa} já está no estacionamento!",
                                     text_color="white")

    def registrar_saida(self):
        placa = self.entry_placa_estacionamento.get()

        if not placa:
            self.resultado.configure(text="Digite uma placa!",
                                     text_color="red")
            return

        if placa in self.estacionados:
            self.estacionados.remove(placa)
            self.resultado.configure(text=f"{placa} saiu do estacionamento",
                                     text_color="red")
            self.atualizar_lista_estacionados()
            self.atualizar_sistema()
        else:
            self.resultado.configure(text=f"{placa} não está no estacionamento!",
                                     text_color="red")

    def atualizar_lista_estacionados(self):
        self.texto_estacionados.delete("1.0", "end")
        for placa in self.estacionados:
            self.texto_estacionados.insert("end", f"{placa}\n")

    def criar_sistema(self):
        aba = self.abas.tab("Sistema")

        self.label_sistema_titulo = ctk.CTkLabel(aba,
                                                 text="Dashboard do Sistema",
                                                 font=ctk.CTkFont(size=16))
        self.label_sistema_titulo.pack(pady=(30, 20))

        self.label_total_veiculos = ctk.CTkLabel(aba,
                                                 text="Veículos cadastrados: 0",
                                                 font=ctk.CTkFont(size=14))
        self.label_total_veiculos.pack(pady=10)

        self.label_estacionados = ctk.CTkLabel(aba,
                                               text="Veículos estacionados: 0",
                                               font=ctk.CTkFont(size=14))
        self.label_estacionados.pack(pady=10)

        self.label_vagas = ctk.CTkLabel(aba,
                                        text="Vagas disponíveis: 20",
                                        font=ctk.CTkFont(size=14))
        self.label_vagas.pack(pady=10)

        self.label_ocupacao = ctk.CTkLabel(aba, text="Ocupação do estacionamento:")
        self.label_ocupacao.pack(pady=(30, 5))

        self.barra_ocupacao = ctk.CTkProgressBar(aba, width=400)
        self.barra_ocupacao.pack(pady=(5, 5))
        self.barra_ocupacao.set(0)

        self.label_porcentagem = ctk.CTkLabel(aba, text="0%")
        self.label_porcentagem.pack(pady=(0, 10))

    def atualizar_sistema(self):
        total_vagas = 20

        self.label_total_veiculos.configure(
            text=f"Veículos cadastrados: {len(self.veiculos)}")
        self.label_estacionados.configure(
            text=f"Veículos estacionados: {len(self.estacionados)}")
        self.label_vagas.configure(
            text=f"Vagas disponíveis: {total_vagas - len(self.estacionados)}")

        ocupacao = len(self.estacionados) / total_vagas
        self.barra_ocupacao.set(ocupacao)
        self.label_porcentagem.configure(text=f"{int(ocupacao * 100)}%")

    def ir_para_sistema(self):
        self.abas.set("Sistema")

    def mudar_modo_dark(self):
        if self.switch_mododark.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def fazer_logout(self):
        self.destroy()
        tela = TelaInicial()
        tela.mainloop()


janela = TelaInicial()
janela.mainloop()
