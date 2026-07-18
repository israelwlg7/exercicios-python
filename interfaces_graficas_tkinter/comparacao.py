import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor

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

        self.abas = ctk.CTkTabview(self)
        self.abas.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.abas.add("Cadastro")
        self.abas.add("Estacionamento")
        self.abas.add("Dashboard")

        self.criar_lateral()
        self.criar_cadastro()
        self.criar_estacionamento()
        self.criar_dashboard()

    def criar_lateral(self):

        titulo = ctk.CTkLabel(
            self.barra_lateral,
            text=f"Usuário\n{self.usuario}",
            font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=20)

    def criar_cadastro(self):

        aba = self.abas.tab("Cadastro")

        self.entry_placa = ctk.CTkEntry(aba,placeholder_text="Placa")
        self.entry_placa.pack(pady=10)

        self.entry_modelo = ctk.CTkEntry(aba,placeholder_text="Modelo")
        self.entry_modelo.pack(pady=10)

        self.entry_cor = ctk.CTkEntry(aba,placeholder_text="Cor")
        self.entry_cor.pack(pady=10)

        self.botao_cadastrar = ctk.CTkButton(aba,text="Cadastrar Veículo",command=self.cadastrar_veiculo)
        self.botao_cadastrar.pack(pady=10)

        self.texto_veiculos = ctk.CTkTextbox(aba,width=500,height=200)
        self.texto_veiculos.pack(pady=10)

    def cadastrar_veiculo(self):

        placa = self.entry_placa.get()
        modelo = self.entry_modelo.get()
        cor = self.entry_cor.get()

        if placa and modelo and cor:

            veiculo = Veiculo(placa,modelo,cor)

            self.veiculos.append(veiculo)

            self.atualizar_lista_veiculos()

            self.entry_placa.delete(0, "end")
            self.entry_modelo.delete(0, "end")
            self.entry_cor.delete(0, "end")

    def atualizar_lista_veiculos(self):

        self.texto_veiculos.delete("1.0", "end")

        for veiculo in self.veiculos:

            self.texto_veiculos.insert("end",f"{veiculo.placa} | {veiculo.modelo} | {veiculo.cor}\n")

    def criar_estacionamento(self):

        aba = self.abas.tab("Estacionamento")

        self.entry_placa_estacionamento = ctk.CTkEntry(aba,placeholder_text="Digite a placa")
        self.entry_placa_estacionamento.pack(pady=10)

        self.botao_entrada = ctk.CTkButton(aba,text="Registrar Entrada",command=self.registrar_entrada)
        self.botao_entrada.pack(pady=5)

        self.botao_saida = ctk.CTkButton(aba,text="Registrar Saída",command=self.registrar_saida)
        self.botao_saida.pack(pady=5)

        self.resultado = ctk.CTkLabel(aba,text="")
        self.resultado.pack(pady=10)

    def registrar_entrada(self):

        placa = self.entry_placa_estacionamento.get()

        if placa not in self.estacionados:

            self.estacionados.append(placa)

            self.resultado.configure(text=f"{placa} entrou no estacionamento",text_color="green")

            self.atualizar_dashboard()

    def registrar_saida(self):

        placa = self.entry_placa_estacionamento.get()

        if placa in self.estacionados:

            self.estacionados.remove(placa)

            self.resultado.configure(text=f"{placa} saiu do estacionamento",text_color="orange")

            self.atualizar_dashboard()

    def criar_dashboard(self):

        aba = self.abas.tab("Dashboard")

        self.label_total_veiculos = ctk.CTkLabel(aba,text="Veículos cadastrados: 0")
        self.label_total_veiculos.pack(pady=20)

        self.label_estacionados = ctk.CTkLabel(aba,text="Veículos estacionados: 0")
        self.label_estacionados.pack(pady=20)

    def atualizar_dashboard(self):

        self.label_total_veiculos.configure(text=f"Veículos cadastrados: {len(self.veiculos)}")

        self.label_estacionados.configure(text=f"Veículos estacionados: {len(self.estacionados)}")

class Login(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("400x300")

        ctk.CTkLabel(self,text="Usuário").pack(pady=10)

        self.campo_usuario = ctk.CTkEntry(self)
        self.campo_usuario.pack()

        ctk.CTkLabel(self,text="Senha").pack(pady=10)

        self.campo_senha = ctk.CTkEntry(self,show="*")
        self.campo_senha.pack()

        self.botao = ctk.CTkButton(self,text="Entrar",command=self.validar_login)
        self.botao.pack(pady=20)

        self.resultado = ctk.CTkLabel(self,text="")
        self.resultado.pack()

    def validar_login(self):

        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()

        if usuario == "israel" and senha == "303002":

            self.destroy()

            app = Aplicativo(usuario)
            app.mainloop()

        else:

            self.resultado.configure(text="Login incorreto",text_color="red")

janela = Login()
janela.mainloop()