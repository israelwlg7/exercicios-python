import tkinter as tk
from PIL import Image, ImageTk

class JanelaComAviao:
    def __init__(self, root):
        self.root = root
        self.root.title("Tal da janela com Avião")
        self.root.geometry("400x300")
        try:
            self.imagem_aviao = Image.open("aviao.png")
            self.imagem_aviao = ImageTk.PhotoImage(self.imagem_aviao)
            self.Label_imagem = tk.Label(self.root, image=self.imagem_aviao)
            self.Label_imagem.pack(pady=20)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")        
            self.Label_imagem = tk.Label(self.root, text="Imagem não encontrada")
            self.Label_imagem.pack(pady=20)
        self.botao_fechar = tk.Button(self.root, text="Sair", command=self.root.destroy)
        self.botao_fechar.pack()
if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = JanelaComAviao(janela_principal)
    janela_principal.mainloop()