import tkinter as tk
from tkinter.font import Font
janela = tk.Tk()

janela.title("Sistema de Cadastro de Usuarios")
janela.geometry("900x600")

# criar o elemento
titulo = tk.Label(text="Meu app", font=Font(size=22, weight="bold", family="Arial"))
# posiciona ele na janela
titulo.pack(pady=(20, 20))

titulo = tk.Label(text="Bem vindo")
titulo.pack(pady=(20, 20))
janela.mainloop()