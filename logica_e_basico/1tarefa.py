import tkinter as tk
import sqlite3

class Janela:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Tarefas")
        self.master.geometry("400x700")

        
        self.conn = sqlite3.connect("tarefas.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        
        self.label_tarefa = tk.Label(master, text="Tarefa:")
        self.label_tarefa.pack()

        self.entry_tarefa = tk.Entry(master)
        self.entry_tarefa.pack()

        self.button_adicionar = tk.Button(master, text="Adicionar", command=self.adicionar_tarefa)
        self.button_adicionar.pack()

        self.listbox_tarefas = tk.Listbox(master)
        self.listbox_tarefas.pack(fill=tk.BOTH, expand=True)

        self.button_remover = tk.Button(master, text="Remover", command=self.remover_tarefa)
        self.button_remover.pack()

        self.button_atualizar = tk.Button(master, text="Atualizar", command=self.update_tarefa)
        self.button_atualizar.pack()

        self.carregar_tarefas()

    def criar_tabela(self):
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL)""")
        self.conn.commit()

    def adicionar_tarefa(self):
        descricao = self.entry_tarefa.get().strip()
        if descricao:
            self.cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
            self.conn.commit()
            self.entry_tarefa.delete(0, tk.END)
            self.carregar_tarefas()

    def remover_tarefa(self):
        selected_index = self.listbox_tarefas.curselection()
        if selected_index:
            tarefa_id = self.listbox_tarefas.get(selected_index).split(":")[0]
            self.cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
            self.conn.commit()
            self.carregar_tarefas()
    def update_tarefa(self):
        selected_index = self.listbox_tarefas.curselection()
        if selected_index:
            tarefa_id = self.listbox_tarefas.get(selected_index).split(":")[0]
            nova_descricao = self.entry_tarefa.get().strip()
            if nova_descricao:
                self.cursor.execute("UPDATE tarefas SET descricao = ? WHERE id = ?", (nova_descricao, tarefa_id))
                self.conn.commit()
                self.entry_tarefa.delete(0, tk.END)
                self.carregar_tarefas()

    def carregar_tarefas(self):
        self.listbox_tarefas.delete(0, tk.END)
        for row in self.cursor.execute("SELECT id, descricao FROM tarefas"):
            self.listbox_tarefas.insert(tk.END, f"{row[0]}: {row[1]}")
    def fechar_conexao(self):
        self.conn.close()
        self.master.destroy()


root = tk.Tk()
app = Janela(root)
root.protocol("WM_DELETE_WINDOW", app.fechar_conexao)
root.mainloop()