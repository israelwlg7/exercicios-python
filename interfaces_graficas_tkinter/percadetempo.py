import tkinter as tk
from tkinter import messagebox

def salvar_cadastro():
    nome = ent_nome.get()
    email = ent_email.get()

    if nome == "" or email == "":
        messagebox.showwarning("Atenção", " Por favor preencha todos os campos")
    else:
        messagebox.showinfo("Sucesso", f"Aluno: {nome}\nE-mail: {email}\nCadastro com sucesso")
janela = tk.Tk()
janela.title("Sistema de cadastro - SENAC")
janela.geometry("300x200")
janela.config(padx=20, pady=20)
tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky="w", pady=5)
ent_nome = tk.Entry(janela, width=30)
ent_nome.grid(row=0, column=1, pady=5)
tk.Label(janela, text="E-mail:").grid(row=1, column=0, sticky="w", pady=5)
ent_email = tk.Entry(janela, width=30)
ent_email.grid(row=1, column=1, pady=5)

btn_salvar = tk.Button(janela, text="Cadastrar aluno", command=salvar_cadastro, bg="blue", fg="white")
btn_salvar.grid(row=2, column=0, columnspan=2, pady=20)

janela.mainloop()