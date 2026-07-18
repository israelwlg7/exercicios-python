import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Cadastro - Senac")
        self.geometry("300x200")
        self.config(padx=20, pady=20)
        ctk.CTkLabel(self,
                     text="Nome").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_nome = ctk.CTkEntry(self,
                                     width=250)
        self.ent_nome.grid(row=0, column=1, pady=5)
        ctk.CTkLabel(self,
                     text="Email:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_email = ctk.CTkEntry(self,
                                      width=250)
        self.ent_email.grid(row=1, column=1, pady=5)

        self.btn_salvar = ctk.CTkButton(self,
                                        text="Cadastrar Aluno",
                                        command=self.salvar_cadastro)
        self.btn_salvar.grid(row=2, column=0, columnspan=2, pady=20)
    def salvar_cadastro(self):
        self.nome = self.ent_nome.get()
        self.email = self.ent_email.get()

        if self.nome == "" or self.email == "":
            messagebox.showwarning("Atenção", "Por favor preencha todos os Campos")
        else:
            messagebox.showinfo("Sucesso", f"Aluno: {self.nome}\nE-mail: {self.email}\nCadastro com Sucesso")
app = Janela()
app.mainloop()