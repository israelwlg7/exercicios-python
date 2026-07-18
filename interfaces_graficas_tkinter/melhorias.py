import customtkinter as ctk
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
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))
        
        self.frame = ctk.CTkFrame(self,
                                  width=400,
                                  height=500,
                                  corner_radius=20,
                                  fg_color=("#FFFFFF", "#0F172A"),
                                  border_width=1,
                                  border_color=("#CBD5E1", "#334155"))
        self.frame.place(relx=0.5,
                         rely=0.5,
                         anchor="center")
        self.frame.pack_propagate(False)

        self.logo = ctk.CTkLabel(self.frame,
                                 text="🅿",
                                 font=ctk.CTkFont(size=65),
                                 text_color=("#2563EB", "#2563EB"))
        self.logo.pack(pady=(25, 5))

        self.label_titulo = ctk.CTkLabel(self.frame,
                                         text="Bem-vindo!",
                                         font=ctk.CTkFont(size=30, weight="bold"),
                                        text_color=("#0F172A", "#F9FAFB"))
        self.label_titulo.pack()

        self.label_subtitulo = ctk.CTkLabel(self.frame,
                                            text="Sistema de Estacionamento",
                                            font=ctk.CTkFont(size=14),
                                            text_color=("#475569", "#9CA3AF"))
        self.label_subtitulo.pack(pady=(4, 25))

        self.botao_login = ctk.CTkButton(self.frame,
                                         text="🔐  Fazer Login",
                                         width=300,
                                         height=46,
                                         corner_radius=14,
                                         fg_color=("#2563EB", "#2563EB"),
                                         hover_color=("#1D4ED8", "#1D4ED8"),
                                         font=ctk.CTkFont(size=15, weight="bold"),
                                         command=self.abrir_login)
        self.botao_login.pack(pady=10)

        self.botao_cadastro = ctk.CTkButton(self.frame,
                                            text="👤  Criar Conta",
                                            width=300,
                                            height=46,
                                            corner_radius=14,
                                            fg_color=("#64748B","#4B5563"),
                                            hover_color=("#15803D", "#15803D"),
                                            font=ctk.CTkFont(size=15, weight="bold"),
                                            command=self.abrir_cadastro)
                                            
        self.botao_cadastro.pack(pady=7)

        self.botao_visitante = ctk.CTkButton(self.frame,
                                             text="👁  Entrar como Visitante",
                                             width=300,
                                             height=46,
                                             corner_radius=14,
                                             fg_color=("#64748B", "#4B5563"),
                                             hover_color=("#475569", "#374151"),
                                             font=ctk.CTkFont(size=15,
                                                              weight="bold"),
                                             command=self.entrar_visitante)
        self.botao_visitante.pack(pady=7)

        self.switch_tema = ctk.CTkSwitch(self,
                                         text="🌙 Modo Escuro",
                                         font=ctk.CTkFont(size=12),
                                         text_color=("#0F172A", "#F9FAFB"),
                                         command=self._toggle_tema)
        self.switch_tema.place(relx=0.95,
                               rely=0.04,
                               anchor="ne")
        if ctk.get_appearance_mode().lower() =="dark":
            self.switch_tema.select()
        self.label_rodape = ctk.CTkLabel(self,
                                         text="PY • Project Senac",
                                         font=ctk.CTkFont(size=11),
                                         text_color=("#475569", "#9CA3AF"))
        self.label_rodape.place(relx=0.5, rely=0.97,
                                anchor="center")
    def _toggle_tema(self):
        ctk.set_appearance_mode("dark" if self.switch_tema.get() == 1 else "light")
        

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
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))
        
        self.frame = ctk.CTkFrame(self,
                                  width=390,
                                  height=500,
                                  corner_radius=20,
                                  fg_color=("#FFFFFF", "#0F172A"),
                                  border_width=1,
                                  border_color=("#CBD5E1", "#334155"))
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack_propagate(False)
        self.logo = ctk.CTkLabel(self.frame,
                                 text="👤",
                                 font=ctk.CTkFont(size=50))
        self.logo.pack(pady=(20, 5))
        self.label_titulo = ctk.CTkLabel(self.frame,
                                         text="Criar Conta",
                                         font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.pack(pady=(0, 15))
        self.campo_usuario = self._criar_entry(self.frame,
                                               "👤  Nome de usuário")
        self.campo_senha = self._criar_entry(self.frame,
                                            "🔒  Senha", show="*")
        self.campo_confirmar = self._criar_entry(self.frame,
                                                "🔒  Confirmar senha", show="*")
        self.resultado = ctk.CTkLabel(self.frame,
                                      text="",
                                      font=ctk.CTkFont(size=14))
        self.resultado.pack(pady=(6, 0))

        self.botao_cadastrar = ctk.CTkButton(self.frame,
                                             text="✅  Criar Conta",
                                             width=300,
                                             height=46,
                                             fg_color=("#16A34A", "#22C55E"),
                                             hover_color=("#15803D", "#15803D"),
                                             font=ctk.CTkFont(size=15, weight="bold"),
                                             command=self.fazer_cadastro)
        self.botao_cadastrar.pack(pady=(10, 6))

        self.botao_voltar = ctk.CTkButton(self.frame,
                                          text="↩  Voltar",
                                          width=300,
                                          height=40,
                                          corner_radius=14,
                                          fg_color=("#64748B", "#4B5563"),
                                          hover_color=("#475569", "#374151"),
                                          font=ctk.CTkFont(size=14),
                                          command=self.voltar)
        self.botao_voltar.pack(pady=4)
    def _criar_entry(self, parent, placeholder, show=""):
        entry = ctk.CTkEntry(parent,
                             placeholder_text=placeholder,
                             width=300,
                             height=44,
                             corner_radius=12,
                             fg_color=("#F1F5F9", "#1E293B"),
                             border_color=("#CBD5E1", "#334155"),
                             text_color=("#0F172A", "#F9FAFB"),
                             font=ctk.CTkFont(size=14), show=show)
        entry.pack(pady=6)
        return entry
    
    def fazer_cadastro(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        confirmar = self.campo_confirmar.get()
        self._registrar_usuario(usuario, senha, confirmar)

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
        self.after(1000, self.voltar)

    def voltar(self):
        self.destroy()
        tela = TelaInicial()
        tela.mainloop()


class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login - Sistema de Estacionamento")
        self.geometry("900x620")
        self.resizable(False, False)
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))

        frame = ctk.CTkFrame(self,
                             width=390,
                             height=450,
                             corner_radius=20,
                             fg_color=("#ffffff", "#0F172A"),
                             border_width=1, border_color=("#CBD5E1", "#334155"))
        frame.place(relx=0.5, rely=0.5, anchor="center")
        frame.pack_propagate(False)
        
        ctk.CTkLabel(frame,
                     text="🔐",
                     font=ctk.CTkFont(size=50)).pack(pady=(20, 5))
        ctk.CTkLabel(frame,
                     text="Fazer Login",
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(0, 15))
        self.campo_usuario = self._entry(frame, "👤  Usuário")
        self.campo_senha = self._entry(frame, "🔒  Senha", show="*")
        self.resultado = ctk.CTkLabel(frame,
                                      text="",
                                      font=ctk.CTkFont(size=14))
        self.resultado.pack(pady=(6, 0))

        ctk.CTkButton(frame,
                      text="🚀  Entrar", width=300, height=46,
                      corner_radius=14, fg_color="#2563EB", hover_color="#1D4ED8",
                      font=ctk.CTkFont(size=15, weight="bold"),
                      command=self.validar_login).pack(pady=(10, 6))
        ctk.CTkButton(frame,
                      text="↩  Voltar",
                      width=300,
                      height=40,
                      corner_radius=14,
                      fg_color="#64748B",
                      hover_color="#475569",
                      font=ctk.CTkFont(size=14),
                      command=self.voltar).pack(pady=4)
    def _entry(self, parent, placeholder):
        entry = ctk.CTkEntry(parent,
                             placeholder_text=placeholder,
                             width=300,
                             height=44,
                             corner_radius=12,
                             fg_color=("#F1F5F9", "#1E293B"),
                             border_color=("#CBD5E1", "#334155"),
                             text_color=("#0F172A", "#F9FAFB"),
                             font=ctk.CTkFont(size=14))
        entry.pack(pady=6)
        return entry

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
        self.estacionados = []
        self.veiculos =  []

        self.title("Sistema de Estacionamento")
        self.geometry("900x600")
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.barra_lateral = ctk.CTkFrame(self, width=220,
                                          corner_radius=0,
                                          fg_color=("#FFFFFF", "#0F172A"))
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")
        self.barra_lateral.grid_propagate(False)

        content = ctk.CTkFrame(self,
                               fg_color=("#F8FAFC", "#0B0F19"),
                               corner_radius=0)
        
        content.grid(row=0, column=1, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)
        
        self.paginas = {}
        for nome in ("Sistema", "Cadastro", "Estacionamento"):
            pag = ctk.CTkFrame(content,
                               fg_color=("#F8FAFC", "#0B0F19"))
            pag.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
            self.paginas[nome] = pag

        self._build_sidebar()
        self._build_sistema()
        self._build_cadastro()
        self._build_estacionamento()
        self._mostrar("Sistema")

    def _mostrar(self, nome):
        for pag in self.paginas.values(): pag.grid_remove()
        self.paginas[nome].grid()
    def _titulo_pagina(self, parent, texto):
        ctk.CTkLabel(parent,
                     text=texto,
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB"),
                     anchor="w").pack(fill="x", pady=(10, 20))
    def _card_frame(self, parent):
        return ctk.CTkFrame(parent,
                            corner_radius=18,
                            fg_color=("#F1F5F9", "#1E293B"),
                            border_width=1,
                            border_color=("#CBD5E1", "#334155"))
    def _entry_app(self, parent, placeholder):
        novo = ctk.CTkEntry(parent,
                            placeholder_text=placeholder,
                            width=260,
                            height=44,
                            corner_radius=14,
                            fg_color=("#FFFFFF", "#0F172A"),
                            border_color=("#CBD5E1", "#334155"),
                            text_color=("#0F172A", "#F9FAFB"),
                            font=ctk.CTkFont(size=14))
        novo.pack(pady=7)
        return novo
    def _build_sidebar(self):

        ctk.CTkLabel(self.sidebar,
                     text="🅿 Parking",
                     font=ctk.CTkFont(size=22, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(28, 4))

        ctk.CTkFrame(self.sidebar,
                     height=1,
                     fg_color=("#CBD5E1", "#334155")).pack(fill="x", padx=20, pady=8)

        ctk.CTkLabel(self.sidebar, text=f"👤 {self.usuario}",
                     font=ctk.CTkFont(size=14),
                     text_color=("#475569", "#9CA3AF")).pack(pady=(4, 16))

        ctk.CTkButton(self.sidebar,
                      text="📊 Sistema",
                      width=180,
                      height=42,
                      corner_radius=12,
                      fg_color="transparent",
                      hover_color=("#F1F5F9", "#1E293B"),
                      anchor="w",
                      font=ctk.CTkFont(size=14),
                      text_color=("#0F172A", "#F9FAFB"),
                      command=lambda: self._mostrar("Sistema")).pack(pady=3, padx=16)

        ctk.CTkButton(self.sidebar,
                      text="🚗 Cadastro",
                      width=180,
                      height=42,
                      corner_radius=12,
                      fg_color="transparent",
                      hover_color=("#F1F5F9", "#1E293B"),
                      anchor="w",
                      font=ctk.CTkFont(size=14),
                      text_color=("#0F172A", "#F9FAFB"),
                      command=lambda: self._mostrar("Cadastro")).pack(pady=3, padx=16)

        ctk.CTkButton(self.sidebar,
                      text="🅿 Estacionamento",
                      width=180,
                      height=42,
                      corner_radius=12,
                      fg_color="transparent",
                      hover_color=("#F1F5F9", "#1E293B"),
                      anchor="w",
                      font=ctk.CTkFont(size=14),
                      text_color=("#0F172A", "#F9FAFB"),
                      command=lambda: self._mostrar("Estacionamento")).pack(pady=3, padx=16)
        
    def _build_sistema(self):
        p = self.paginas["Sistema"]
        self._titulo_pagina(p, "📊  Dashboard do Sistema")

        cards_frame = ctk.CTkFrame(p, fg_color="transparent")
        cards_frame.pack(fill="x")

        self.nums_dashboard = []

        card1 = self._card_frame(cards_frame, width=200, height=130)
        card1.grid(row=0, column=0, padx=8, sticky="nsew")
        cards_frame.grid_columnconfigure(0, weight=1)
        card1.pack_propagate(False)

        ctk.CTkLabel(card1, text="🚗", font=ctk.CTkFont(size=28)).pack(pady=(16, 2))
        lbl1 = ctk.CTkLabel(card1,
                            text="0",
                            font=ctk.CTkFont(size=36, weight="bold"),
                            text_color="#2563EB")
        lbl1.pack()
        ctk.CTkLabel(card1,
                    text="Veículos cadastrados",
                    font=ctk.CTkFont(size=12),
                    text_color=("#475569", "#9CA3AF")).pack(pady=(0, 10))
        self.nums_dashboard.append(lbl1)

        card2 = self._card_frame(cards_frame, width=200, height=130)
        card2.grid(row=0, column=1, padx=8, sticky="nsew")
        cards_frame.grid_columnconfigure(1, weight=1)
        card2.pack_propagate(False)

        ctk.CTkLabel(card2,
                     text="🅿",
                     font=ctk.CTkFont(size=28)).pack(pady=(16, 2))
        lbl2 = ctk.CTkLabel(card2,
                            text="0",
                            font=ctk.CTkFont(size=36, weight="bold"),
                            text_color="#22C55E")
        lbl2.pack()
        ctk.CTkLabel(card2,
                     text="Veículos estacionados",
                    font=ctk.CTkFont(size=12),
                    text_color=("#475569", "#9CA3AF")).pack(pady=(0, 10))
        self.nums_dashboard.append(lbl2)

        card3 = self._card_frame(cards_frame, width=200, height=130)
        card3.grid(row=0, column=2, padx=8, sticky="nsew")
        cards_frame.grid_columnconfigure(2, weight=1)
        card3.pack_propagate(False)

        ctk.CTkLabel(card3,
                     text="✅",
                     font=ctk.CTkFont(size=28)).pack(pady=(16, 2))
        lbl3 = ctk.CTkLabel(card3, text="20",
                         font=ctk.CTkFont(size=36, weight="bold"),
                         text_color="#8B5CF6")
        lbl3.pack()
        ctk.CTkLabel(card3,
                     text="Vagas disponíveis",
                    font=ctk.CTkFont(size=12),
                    text_color=("#475569", "#9CA3AF")).pack(pady=(0, 10))
        self.nums_dashboard.append(lbl3)

        occ = self._card_frame(p)
        occ.pack(fill="x", pady=(24, 15), padx=8)

        ctk.CTkLabel(occ,
                 text="Ocupação do estacionamento",
                 font=ctk.CTkFont(size=14),
                 text_color=("#0F172A", "#F9FAFB")).pack(pady=(16, 8))

        self.barra_ocupacao = ctk.CTkProgressBar(occ,
                                                 width=500,
                                                 height=16,
                                                 corner_radius=8,
                                                 progress_color="#2563EB")
        self.barra_ocupacao.pack(padx=30)
        self.barra_ocupacao.set(0)

        self.label_pct = ctk.CTkLabel(occ,
                                      text="0%",
                                      font=ctk.CTkFont(size=18, weight="bold"),
                                      text_color="#2563EB")
        self.label_pct.pack(pady=(6, 16))

    def _build_cadastro(self):
        p = self.pagina["Cadastro"]
        self._titulo_pagina(p, "🚗  Cadastro de Veículos")

        row = ctk.CTkFrame(p,
                           fg_color="transparent")
        row.pack(fill="both",
                 expand=True)
        row.grid_columnconfigure((0, 1), weight=1)
        row.grid_rowconfigure(0, weight=1)

        form = self._card_frame(row)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        
        ctk.CTkLabel(form,
                     text="Novo Veículo",
                     font=ctk.CTkFont(size=16,
                    weight="bold"),
                    text_color=("#0F172A", "#F9FAFB")).pack(pady=(20, 12))
        
        self.entry_placa  = self._entry_app(form, "Placa do veículo")
        self.entry_modelo = self._entry_app(form, "Modelo do veículo")
        self.entry_cor    = self._entry_app(form, "Cor do veículo")

        self.res_cadastro = ctk.CTkLabel(form,
                                         text="",
                                         font=ctk.CTkFont(size=14))
        self.res_cadastro.pack(pady=(6, 0))

        ctk.CTkButton(form,
                      text="✅ Cadastrar Veículo",
                      width=260,
                      height=44,
                      corner_radius=14,
                      fg_color="#16A34A",
                      hover_color="#15803D",
                      font=ctk.CTkFont(size=14, weight="bold"),
                      command=self._cadastrar).pack(pady=(12, 20))
        
        lista = self._card_frame(row)
        lista.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        ctk.CTkLabel(lista,
                     text="Veículos Cadastrados",
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(20, 8))
        
        self.texto_veiculos = ctk.CTkTextbox(lista, corner_radius=12,
                                              font=ctk.CTkFont(size=14),
                                              fg_color=("#FFFFFF", "#0F172A"),
                                              text_color=("#0F172A", "#F9FAFB"))
        self.texto_veiculos.pack(fill="both", expand=True, padx=14, pady=(0, 14))