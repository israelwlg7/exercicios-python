import customtkinter as ctk
import tkinter as tk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Seleção de Curso")
        self.geometry("400x450")
        self.var_curso = tk.StringVar(value="Informatica")
        ctk.CTkLabel(self,
                     text="Escolha seu Curso",
                     font=ctk.CTkFont(size=12)).pack()
        ctk.CTkRadioButton(self,
                           text="Informatica",
                           variable=self.var_curso,
                           value="Informatica").pack()
        ctk.CTkRadioButton(self,
                           text="Redes",
                           variable=self.var_curso,
                           value="Redes").pack()
        ctk.CTkRadioButton(self,
                           text="Desing",
                           variable=self.var_curso,
                           value="Desing").pack()
        ctk.CTkButton(self,
                      text="Confirmar",
                      command=self.verificar_selecao).pack(pady=20)

    def verificar_selecao(self):
        self.escolha = self.var_curso.get()
        print(f"Curso selecionado: {self.escolha}")
app = Janela()
app.mainloop()

        