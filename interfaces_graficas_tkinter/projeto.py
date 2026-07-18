class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
    def Registrar_veiculo(self):
        self.veiculos = []
        self.estacionados = []
class Adicionar(Veiculo):
    def __init__(self, adicionar, placa, modelo, cor):
        super().__init__(self, placa, modelo, cor)

        self.veiculos.append(Veiculo)
        self.estacionados.append(placa)
        self.estacionados.remove(placa)

import customtkinter as ctk
import time
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class Login(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("400x300")

        ctk.CTkLabel(
            self,
            text="Usuário"
        ).pack(pady=10)

        self.campo_usuario = ctk.CTkEntry(self)
        self.campo_usuario.pack()

        ctk.CTkLabel(
            self,
            text="Senha"
        ).pack(pady=10)

        self.campo_senha = ctk.CTkEntry(
            self,
            show="*"
        )
        self.campo_senha.pack()

        self.botao = ctk.CTkButton(
            self,
            text="Entrar",
            command=self.validar_login
        )
        self.botao.pack(pady=20)

        self.resultado = ctk.CTkLabel(
            self,
            text=""
        )
        self.resultado.pack()

    def validar_login(self):

        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()

        if usuario == "israel" and senha == "303002":

            self.destroy()  # fecha login

            app = Aplicativo(usuario)
            app.mainloop()

        else:

            self.resultado.configure(
                text="Login incorreto",
                text_color="red"
            )


janela = Login()
janela.mainloop()

class Aplicativo(ctk.CTk):
    def __init__(self,  usuario):
        super().__init__()
        self.title("Sistema de Estacionamento")
        self.geometry("900x600")
        self.usuario = usuario  
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        self.janela_abas = ctk.CTkTabview(self)
        self.janela_abas.grid(row=0, column=1, sticky="nsew", padx=10)

        self.janela_abas.add("Perfil")
        self.janela_abas.add("Dashboard")

        self.criar_lateral()
        self.criar_perfil()
        self.criar_dashboard()

    def criar_lateral(self):

        self.label_usuario = ctk.CTkLabel(
            self.barra_lateral,
            text=f"Usuário:\n{self.usuario}",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label_usuario.pack(pady=20)

    def criar_perfil(self):

        aba = self.janela_abas.tab("Perfil")

        self.entry_nome = ctk.CTkEntry(
            aba,
            placeholder_text="Digite seu nome"
        )
        self.entry_nome.pack(pady=20)

    def criar_dashboard(self):

        aba = self.janela_abas.tab("Dashboard")

        self.barra = ctk.CTkProgressBar(aba)
        self.barra.pack(pady=20)
        self.barra.set(0)

        self.botao = ctk.CTkButton(
            aba,
            text="Carregar",
            command=self.carregar
        )
        self.botao.pack()

    def carregar(self):

        for i in range(100):
            time.sleep(0.02)
            self.barra.set((i + 1) / 100)
            self.update()

