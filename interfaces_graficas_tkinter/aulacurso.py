import tkinter as tk

def verificar_selecao():
    escolha = var_curso.get()
    print(f"Curso selecionado: {escolha}")

janela = tk.Tk()
janela.title("Seleção de Curso")

var_curso = tk.StringVar(value="Informatica")
tk.Label(janela, text="Eescolha seu curso", font=("Arial", 12)).pack()

tk.Radiobutton(janela, text="Informatica", variable=var_curso, value="Informatica").pack()
tk.Radiobutton(janela, text="Redes", variable=var_curso, value="Redes").pack()
tk.Radiobutton(janela, text="Desing", variable=var_curso, value="Desing").pack()

tk.Button(janela, text="Confirmar", command=verificar_selecao).pack()

janela.mainloop()