import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Cadastro')
        self.geometry('300x300')
        self.label_usuario = ctk.CTkLabel(self, text="Usuario")
        self.label_usuario.pack(pady=10)
        self.campo_usuario = ctk.CTkEntry(self,
                                          placeholder_text="Digite o seu usuario")
        self.campo_usuario.pack(pady=10)
        self.campo_senha = ctk.CTkLabel(self,
                                        text="Senha")
        self.campo_senha.pack(pady=10)
        self.campo_senha = ctk.CTkEntry(self,
                                        placeholder_text="Digite a sua senha")
        self.campo_senha.pack(pady=10)
        self.botao_login = ctk.CTkButton(self,
                                        text="Login",
                                        command=self.validar_login)
        self.botao_login.pack(pady=10)
        self.resultado_login = ctk.CTkLabel(self,
                                            text="")
        self.resultado_login.pack(pady=10)
    def validar_login(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        if usuario == "israel" and senha == "303002":
            self.resultado_login.configure(text="Login feito com Suecesso!",
                                           text_color="green")
        else:
            self.resultado_login.configure(text="Login incorreto",
                                           text_color="red")
janela = Login()
janela.mainloop()
