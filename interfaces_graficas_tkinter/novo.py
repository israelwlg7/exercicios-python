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
                                        text="")
        self.subtitulo.pack(pady=(0, 5))
        self.botao_principal = ctk.CTkButton(self.barra_lateral,
                                                text="Sistema Principal",
                                                command=self.ir_para_sistema)
        self.botao_principal.pack(pady=(30,30), padx=(10, 10))
        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral,
                                                text="Modo Escuro",
                                                command=self.mudar_modo_dark)
        self.switch_mododark.pack(pady=(10, 10), side="bottom")
        self.switch_mododark.select()

    def criar_cadastro(self):
        aba = self.abas.tab("Cadastro")

        self.entry_placa = ctk.CTkEntry(aba,
                                        placeholder_text="Placa")
        self.entry_placa.pack(pady=10)

        self.entry_modelo = ctk.CTkEntry(aba,
                                        placeholder_text="Modelo")
        self.entry_modelo.pack(pady=10)

        self.entry_cor = ctk.CTkEntry(aba, placeholder_text="Cor")
        self.entry_cor.pack(pady=10)
            
        self.botao_cadastrar = ctk.CTkButton(aba,
                                                text="Cadastrar Veículo",
                                                command=self.cadastrar_veiculo)
        self.texto_veiculos = ctk.CTkTextbox(aba,
                                                width=500,
                                                height=200)
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
    def atualizar_lista_veiculos(self):
        self.texto_veiculos.delete("1.0", "end")

        for veiculo in self.veiculos:
                self.texto_veiculos.insert("end", f"{veiculo.placa} | {veiculo.modelo} | {veiculo.cor}\n")
    def criar_estacionamento(self):
            aba = self.abas.tab("Estacionamento")

            self.entry_placa_estacionamento = ctk.CTkEntry(aba,
                                                           placeholder_text="Digite a placa Do Seu Carro")
            self.entry_placa_estacionamento.pack(pady=10)
            self.botao_entrada = ctk.CTkButton(aba, 
                                               text="Registrar Entrada",
                                               command=self.registrar_entrada)
            self.botao_entrada.pack(pady=5)
            
            self.botao_saida = ctk.CTkButton(aba,
                                             text="Registrar Saída",
                                             command=self.registrar_saida)
            self.botao_saida.pack(pady=10) 

    def registrar_entrada(self):
            placa = self.entry_placa_estacionamento.get()

            if placa not in self.estacionados:
                self.estacionados.append(placa)
                self.resultado.configure(text=f"{placa} entrou no estacionamento",text_color="green")
                self.atualizar_sistema()

    def registrar_saida(self):
            placa = self.entry_placa_estacionamento.get()

            if placa in self.estacionados:
                self.estacionados.remove(placa)
                self.resultado.configure(text=f"{placa} saiu do estacionamento",text_color="red")
                self.atualizar_sistema()
                