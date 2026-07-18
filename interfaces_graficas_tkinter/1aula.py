import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

usuarios_cadastrados = []


# ─── MODELO ───────────────────────────────────────────────
class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor


# ─── TELA INICIAL ─────────────────────────────────────────
class TelaInicial(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Estacionamento")
        self.geometry("900x620")
        self.resizable(False, False)
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))

        frame = ctk.CTkFrame(self, width=380, height=470, corner_radius=20,
                             fg_color=("#FFFFFF", "#0F172A"),
                             border_width=1, border_color=("#CBD5E1", "#334155"))
        frame.place(relx=0.5, rely=0.5, anchor="center")
        frame.pack_propagate(False)

        ctk.CTkLabel(frame, text="🅿", font=ctk.CTkFont(size=55),
                     text_color="#2563EB").pack(pady=(25, 5))
        ctk.CTkLabel(frame, text="Bem-vindo!",
                     font=ctk.CTkFont(size=30, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack()
        ctk.CTkLabel(frame, text="Sistema de Estacionamento",
                     font=ctk.CTkFont(size=14),
                     text_color=("#475569", "#9CA3AF")).pack(pady=(4, 25))

        botoes = [
            ("🔐  Fazer Login",          "#2563EB", "#1D4ED8", self.abrir_login),
            ("👤  Criar Conta",          "#16A34A", "#15803D", self.abrir_cadastro),
            ("👁  Entrar como Visitante", "#64748B", "#475569", self.entrar_visitante),
        ]
        for texto, cor, hover, cmd in botoes:
            ctk.CTkButton(frame, text=texto, width=300, height=46,
                          corner_radius=14, fg_color=cor, hover_color=hover,
                          font=ctk.CTkFont(size=15, weight="bold"),
                          command=cmd).pack(pady=7)

        self.switch_tema = ctk.CTkSwitch(self, text="🌙 Modo Escuro",
                                         font=ctk.CTkFont(size=12),
                                         text_color=("#0F172A", "#F9FAFB"),
                                         command=self._toggle_tema)
        self.switch_tema.place(relx=0.95, rely=0.04, anchor="ne")
        if ctk.get_appearance_mode().lower() == "dark":
            self.switch_tema.select()

        ctk.CTkLabel(self, text="v2.0  •  Parking System",
                     font=ctk.CTkFont(size=11),
                     text_color=("#475569", "#9CA3AF")).place(relx=0.5, rely=0.97, anchor="center")

    def _toggle_tema(self):
        ctk.set_appearance_mode("dark" if self.switch_tema.get() == 1 else "light")

    def abrir_login(self):
        self.destroy(); TelaLogin().mainloop()

    def abrir_cadastro(self):
        self.destroy(); TelaCadastro().mainloop()

    def entrar_visitante(self):
        self.destroy(); Aplicativo("Visitante").mainloop()


# ─── TELA CADASTRO ────────────────────────────────────────
class TelaCadastro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro — Sistema de Estacionamento")
        self.geometry("900x620")
        self.resizable(False, False)
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))

        frame = ctk.CTkFrame(self, width=390, height=500, corner_radius=20,
                             fg_color=("#FFFFFF", "#0F172A"),
                             border_width=1, border_color=("#CBD5E1", "#334155"))
        frame.place(relx=0.5, rely=0.5, anchor="center")
        frame.pack_propagate(False)

        ctk.CTkLabel(frame, text="👤", font=ctk.CTkFont(size=50)).pack(pady=(20, 5))
        ctk.CTkLabel(frame, text="Criar Conta",
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(0, 15))

        self.campo_usuario  = self._entry(frame, "👤  Nome de usuário")
        self.campo_senha    = self._entry(frame, "🔒  Senha", show="*")
        self.campo_confirmar = self._entry(frame, "🔒  Confirmar senha", show="*")

        self.resultado = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=14))
        self.resultado.pack(pady=(6, 0))

        ctk.CTkButton(frame, text="✅  Criar Conta", width=300, height=46,
                      corner_radius=14, fg_color="#16A34A", hover_color="#15803D",
                      font=ctk.CTkFont(size=15, weight="bold"),
                      command=self.fazer_cadastro).pack(pady=(10, 6))
        ctk.CTkButton(frame, text="↩  Voltar", width=300, height=40,
                      corner_radius=14, fg_color="#64748B", hover_color="#475569",
                      font=ctk.CTkFont(size=14),
                      command=self.voltar).pack(pady=4)

    def _entry(self, parent, placeholder, show=""):
        e = ctk.CTkEntry(parent, placeholder_text=placeholder,
                         width=300, height=44, corner_radius=12,
                         fg_color=("#F1F5F9", "#1E293B"),
                         border_color=("#CBD5E1", "#334155"),
                         text_color=("#0F172A", "#F9FAFB"),
                         font=ctk.CTkFont(size=14), show=show)
        e.pack(pady=6)
        return e

    def fazer_cadastro(self):
        usuario  = self.campo_usuario.get()
        senha    = self.campo_senha.get()
        confirmar = self.campo_confirmar.get()

        if not usuario or not senha or not confirmar:
            self.resultado.configure(text="Preencha todos os campos!", text_color="#EF4444"); return
        if senha != confirmar:
            self.resultado.configure(text="As senhas não coincidem!", text_color="#EF4444"); return
        if any(u["usuario"] == usuario for u in usuarios_cadastrados):
            self.resultado.configure(text="Usuário já existe!", text_color="#EF4444"); return

        usuarios_cadastrados.append({"usuario": usuario, "senha": senha})
        self.resultado.configure(text="Conta criada com sucesso!", text_color="#22C55E")
        self.after(1000, self.voltar)

    def voltar(self):
        self.destroy(); TelaInicial().mainloop()


# ─── TELA LOGIN ───────────────────────────────────────────
class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login — Sistema de Estacionamento")
        self.geometry("900x620")
        self.resizable(False, False)
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))

        frame = ctk.CTkFrame(self, width=390, height=450, corner_radius=20,
                             fg_color=("#FFFFFF", "#0F172A"),
                             border_width=1, border_color=("#CBD5E1", "#334155"))
        frame.place(relx=0.5, rely=0.5, anchor="center")
        frame.pack_propagate(False)

        ctk.CTkLabel(frame, text="🔐", font=ctk.CTkFont(size=50)).pack(pady=(20, 5))
        ctk.CTkLabel(frame, text="Fazer Login",
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(0, 15))

        self.campo_usuario = self._entry(frame, "👤  Usuário")
        self.campo_senha   = self._entry(frame, "🔒  Senha", show="*")

        self.resultado = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=14))
        self.resultado.pack(pady=(6, 0))

        ctk.CTkButton(frame, text="🚀  Entrar", width=300, height=46,
                      corner_radius=14, fg_color="#2563EB", hover_color="#1D4ED8",
                      font=ctk.CTkFont(size=15, weight="bold"),
                      command=self.validar_login).pack(pady=(10, 6))
        ctk.CTkButton(frame, text="↩  Voltar", width=300, height=40,
                      corner_radius=14, fg_color="#64748B", hover_color="#475569",
                      font=ctk.CTkFont(size=14),
                      command=self.voltar).pack(pady=4)

    def _entry(self, parent, placeholder, show=""):
        e = ctk.CTkEntry(parent, placeholder_text=placeholder,
                         width=300, height=44, corner_radius=12,
                         fg_color=("#F1F5F9", "#1E293B"),
                         border_color=("#CBD5E1", "#334155"),
                         text_color=("#0F172A", "#F9FAFB"),
                         font=ctk.CTkFont(size=14), show=show)
        e.pack(pady=6)
        return e

    def validar_login(self):
        usuario = self.campo_usuario.get()
        senha   = self.campo_senha.get()

        for u in usuarios_cadastrados:
            if u["usuario"] == usuario and u["senha"] == senha:
                self.resultado.configure(text="Login feito com sucesso!", text_color="#22C55E")
                self.after(800, self.abrir_app, usuario)
                return

        self.resultado.configure(text="Usuário ou senha incorretos!", text_color="#EF4444")

    def abrir_app(self, usuario):
        self.destroy(); Aplicativo(usuario).mainloop()

    def voltar(self):
        self.destroy(); TelaInicial().mainloop()


# ─── APP PRINCIPAL ────────────────────────────────────────
class Aplicativo(ctk.CTk):
    TOTAL_VAGAS = 20

    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.veiculos    = []
        self.estacionados = []

        self.title("Sistema de Estacionamento")
        self.geometry("1020x670")
        self.configure(fg_color=("#F8FAFC", "#0B0F19"))
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0,
                                    fg_color=("#FFFFFF", "#0F172A"))
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Área de conteúdo com páginas empilhadas
        content = ctk.CTkFrame(self, fg_color=("#F8FAFC", "#0B0F19"), corner_radius=0)
        content.grid(row=0, column=1, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)

        self.paginas = {}
        for nome in ("Dashboard", "Cadastro", "Estacionamento"):
            f = ctk.CTkFrame(content, fg_color=("#F8FAFC", "#0B0F19"))
            f.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
            self.paginas[nome] = f

        self._build_sidebar()
        self._build_dashboard()
        self._build_cadastro()
        self._build_estacionamento()
        self._mostrar("Dashboard")

    # ── helpers ──────────────────────────────────────────
    def _mostrar(self, nome):
        for f in self.paginas.values(): f.grid_remove()
        self.paginas[nome].grid()

    def _titulo_pagina(self, parent, texto):
        ctk.CTkLabel(parent, text=texto,
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB"),
                     anchor="w").pack(fill="x", pady=(10, 20))

    def _card_frame(self, parent, **kwargs):
        return ctk.CTkFrame(parent, corner_radius=18,
                            fg_color=("#F1F5F9", "#1E293B"),
                            border_width=1, border_color=("#CBD5E1", "#334155"),
                            **kwargs)

    def _entry_app(self, parent, placeholder):
        e = ctk.CTkEntry(parent, placeholder_text=placeholder,
                         width=260, height=44, corner_radius=14,
                         fg_color=("#FFFFFF", "#0F172A"),
                         border_color=("#CBD5E1", "#334155"),
                         text_color=("#0F172A", "#F9FAFB"),
                         font=ctk.CTkFont(size=14))
        e.pack(pady=7)
        return e

    # ── sidebar ──────────────────────────────────────────
    def _build_sidebar(self):
        ctk.CTkLabel(self.sidebar, text="🅿 Parking",
                     font=ctk.CTkFont(size=22, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(28, 4))
        ctk.CTkFrame(self.sidebar, height=1,
                     fg_color=("#CBD5E1", "#334155")).pack(fill="x", padx=20, pady=8)
        ctk.CTkLabel(self.sidebar, text=f"👤  {self.usuario}",
                     font=ctk.CTkFont(size=14),
                     text_color=("#475569", "#9CA3AF")).pack(pady=(4, 16))

        nav = [("📊  Dashboard",       "Dashboard"),
               ("🚗  Cadastro",        "Cadastro"),
               ("🅿  Estacionamento",  "Estacionamento")]
        for texto, pagina in nav:
            ctk.CTkButton(self.sidebar, text=texto, width=180, height=42,
                          corner_radius=12, fg_color="transparent",
                          hover_color=("#F1F5F9", "#1E293B"), anchor="w",
                          font=ctk.CTkFont(size=14),
                          text_color=("#0F172A", "#F9FAFB"),
                          command=lambda p=pagina: self._mostrar(p)).pack(pady=3, padx=16)

        ctk.CTkLabel(self.sidebar, text="").pack(expand=True)

        self.switch_dark = ctk.CTkSwitch(self.sidebar, text="🌙  Modo Escuro",
                                         font=ctk.CTkFont(size=12),
                                         text_color=("#0F172A", "#F9FAFB"),
                                         command=self._toggle_dark)
        self.switch_dark.pack(pady=(0, 10), padx=20)
        if ctk.get_appearance_mode().lower() == "dark":
            self.switch_dark.select()

        ctk.CTkButton(self.sidebar, text="🚪  Sair", width=180, height=40,
                      corner_radius=12, fg_color="#DC2626", hover_color="#B91C1C",
                      font=ctk.CTkFont(size=14),
                      command=self._logout).pack(pady=(4, 20), padx=16)

    # ── dashboard ────────────────────────────────────────
    def _build_dashboard(self):
        p = self.paginas["Dashboard"]
        self._titulo_pagina(p, "📊  Dashboard do Sistema")

        cards_frame = ctk.CTkFrame(p, fg_color="transparent")
        cards_frame.pack(fill="x")

        info_cards = [
            ("🚗", "0", "Veículos cadastrados",  "#2563EB"),
            ("🅿", "0", "Veículos estacionados", "#22C55E"),
            ("✅", "20","Vagas disponíveis",      "#8B5CF6"),
        ]
        self.nums_dashboard = []

        for i, (icon, num, label, cor) in enumerate(info_cards):
            card = self._card_frame(cards_frame, width=200, height=130)
            card.grid(row=0, column=i, padx=8, sticky="nsew")
            cards_frame.grid_columnconfigure(i, weight=1)
            card.pack_propagate(False)

            ctk.CTkLabel(card, text=icon, font=ctk.CTkFont(size=28)).pack(pady=(16, 2))
            lbl = ctk.CTkLabel(card, text=num,
                               font=ctk.CTkFont(size=36, weight="bold"),
                               text_color=cor)
            lbl.pack()
            ctk.CTkLabel(card, text=label, font=ctk.CTkFont(size=12),
                         text_color=("#475569", "#9CA3AF")).pack(pady=(0, 10))
            self.nums_dashboard.append(lbl)

        occ = self._card_frame(p)
        occ.pack(fill="x", pady=(24, 15), padx=8)

        ctk.CTkLabel(occ, text="Ocupação do estacionamento",
                     font=ctk.CTkFont(size=14),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(16, 8))

        self.barra_ocupacao = ctk.CTkProgressBar(occ, width=500, height=16,
                                                  corner_radius=8,
                                                  progress_color="#2563EB")
        self.barra_ocupacao.pack(padx=30)
        self.barra_ocupacao.set(0)

        self.label_pct = ctk.CTkLabel(occ, text="0%",
                                      font=ctk.CTkFont(size=18, weight="bold"),
                                      text_color="#2563EB")
        self.label_pct.pack(pady=(6, 16))

    # ── cadastro ─────────────────────────────────────────
    def _build_cadastro(self):
        p = self.paginas["Cadastro"]
        self._titulo_pagina(p, "🚗  Cadastro de Veículos")

        row = ctk.CTkFrame(p, fg_color="transparent")
        row.pack(fill="both", expand=True)
        row.grid_columnconfigure((0, 1), weight=1)
        row.grid_rowconfigure(0, weight=1)

        # formulário
        form = self._card_frame(row)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        ctk.CTkLabel(form, text="Novo Veículo",
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(20, 12))

        self.entry_placa  = self._entry_app(form, "Placa do veículo")
        self.entry_modelo = self._entry_app(form, "Modelo do veículo")
        self.entry_cor    = self._entry_app(form, "Cor do veículo")

        self.res_cadastro = ctk.CTkLabel(form, text="", font=ctk.CTkFont(size=14))
        self.res_cadastro.pack(pady=(6, 0))

        ctk.CTkButton(form, text="✅  Cadastrar Veículo", width=260, height=44,
                      corner_radius=14, fg_color="#16A34A", hover_color="#15803D",
                      font=ctk.CTkFont(size=14, weight="bold"),
                      command=self._cadastrar).pack(pady=(12, 20))

        # lista
        lista = self._card_frame(row)
        lista.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        ctk.CTkLabel(lista, text="Veículos Cadastrados",
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(20, 8))

        self.texto_veiculos = ctk.CTkTextbox(lista, corner_radius=12,
                                              font=ctk.CTkFont(size=14),
                                              fg_color=("#FFFFFF", "#0F172A"),
                                              text_color=("#0F172A", "#F9FAFB"))
        self.texto_veiculos.pack(fill="both", expand=True, padx=14, pady=(0, 14))

    # ── estacionamento ───────────────────────────────────
    def _build_estacionamento(self):
        p = self.paginas["Estacionamento"]
        self._titulo_pagina(p, "🅿  Controle de Estacionamento")

        row = ctk.CTkFrame(p, fg_color="transparent")
        row.pack(fill="both", expand=True)
        row.grid_columnconfigure((0, 1), weight=1)
        row.grid_rowconfigure(0, weight=1)

        # controle
        ctrl = self._card_frame(row)
        ctrl.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        ctk.CTkLabel(ctrl, text="Registrar Movimento",
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(20, 12))

        self.entry_placa_est = self._entry_app(ctrl, "Placa do veículo")

        self.res_est = ctk.CTkLabel(ctrl, text="", font=ctk.CTkFont(size=14))
        self.res_est.pack(pady=(8, 4))

        btns = ctk.CTkFrame(ctrl, fg_color="transparent")
        btns.pack(pady=(8, 20))

        ctk.CTkButton(btns, text="⬅  Entrada", width=125, height=44,
                      corner_radius=14, fg_color="#16A34A", hover_color="#15803D",
                      font=ctk.CTkFont(size=13, weight="bold"),
                      command=self._entrada).pack(side="left", padx=4)
        ctk.CTkButton(btns, text="➡  Saída", width=125, height=44,
                      corner_radius=14, fg_color="#DC2626", hover_color="#B91C1C",
                      font=ctk.CTkFont(size=13, weight="bold"),
                      command=self._saida).pack(side="left", padx=4)

        # lista
        lista = self._card_frame(row)
        lista.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        ctk.CTkLabel(lista, text="Veículos no Estacionamento",
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=("#0F172A", "#F9FAFB")).pack(pady=(20, 8))

        self.texto_estacionados = ctk.CTkTextbox(lista, corner_radius=12,
                                                  font=ctk.CTkFont(size=14),
                                                  fg_color=("#FFFFFF", "#0F172A"),
                                                  text_color=("#0F172A", "#F9FAFB"))
        self.texto_estacionados.pack(fill="both", expand=True, padx=14, pady=(0, 14))

    # ── ações ─────────────────────────────────────────────
    def _cadastrar(self):
        placa, modelo, cor = self.entry_placa.get(), self.entry_modelo.get(), self.entry_cor.get()
        if not (placa and modelo and cor):
            self.res_cadastro.configure(text="Preencha todos os campos!", text_color="#EF4444"); return

        self.veiculos.append(Veiculo(placa, modelo, cor))
        self.texto_veiculos.insert("end", f"  {placa}  │  {modelo}  │  {cor}\n")
        self.entry_placa.delete(0, "end")
        self.entry_modelo.delete(0, "end")
        self.entry_cor.delete(0, "end")
        self.res_cadastro.configure(text=f"Veículo {placa} cadastrado!", text_color="#22C55E")
        self._atualizar_dashboard()

    def _entrada(self):
        placa = self.entry_placa_est.get()
        if not placa:
            self.res_est.configure(text="Digite uma placa!", text_color="#EF4444"); return
        if placa in self.estacionados:
            self.res_est.configure(text=f"{placa} já está aqui!", text_color="#9CA3AF"); return

        self.estacionados.append(placa)
        self.texto_estacionados.insert("end", f"  🚗  {placa}\n")
        self.res_est.configure(text=f"{placa} entrou!", text_color="#22C55E")
        self._atualizar_dashboard()

    def _saida(self):
        placa = self.entry_placa_est.get()
        if not placa:
            self.res_est.configure(text="Digite uma placa!", text_color="#EF4444"); return
        if placa not in self.estacionados:
            self.res_est.configure(text=f"{placa} não está aqui!", text_color="#EF4444"); return

        self.estacionados.remove(placa)
        self._atualizar_lista_estacionados()
        self.res_est.configure(text=f"{placa} saiu!", text_color="#EF4444")
        self._atualizar_dashboard()

    def _atualizar_lista_estacionados(self):
        self.texto_estacionados.delete("1.0", "end")
        for p in self.estacionados:
            self.texto_estacionados.insert("end", f"  🚗  {p}\n")

    def _atualizar_dashboard(self):
        n_cad = len(self.veiculos)
        n_est = len(self.estacionados)
        n_vag = self.TOTAL_VAGAS - n_est
        occ   = n_est / self.TOTAL_VAGAS

        self.nums_dashboard[0].configure(text=str(n_cad))
        self.nums_dashboard[1].configure(text=str(n_est))
        self.nums_dashboard[2].configure(text=str(n_vag))
        self.barra_ocupacao.set(occ)
        self.label_pct.configure(text=f"{int(occ * 100)}%")

        if occ >= 0.85:
            cor = "#EF4444"
        elif occ >= 0.5:
            cor = "#F59E0B"
        else:
            cor = "#2563EB"

        self.barra_ocupacao.configure(progress_color=cor)
        self.label_pct.configure(text_color=cor)

    def _toggle_dark(self):
        ctk.set_appearance_mode("dark" if self.switch_dark.get() == 1 else "light")

    def _logout(self):
        self.destroy(); TelaInicial().mainloop()


# ─── INÍCIO ───────────────────────────────────────────────
TelaInicial().mainloop()