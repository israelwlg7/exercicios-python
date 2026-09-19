
import customtkinter as ctk
import random


palavras = [
    "cachorro",
    "gato",
    "casa",
    "carro",
    "mesa",
    "cadeira",
    "copo",
    "caneta",
    "livro",
    "telefone",
]


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Game(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Jogo: Quem é o impostor")
        self.geometry("400x300")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):

        self.start_button = ctk.CTkButton(
            self,
            text="Começar",
            command=self.start_game
        )

        self.start_button.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

    def start_game(self):

        self.start_button.grid_forget()

        self.play_game()

    # Mostrar a palavra secreta para cada jogador
    def play_game(self):

        # Sorteia a palavra
        self.palavra_secreta = random.choice(palavras)

        # Sorteia o impostor
        self.impostor = random.randint(1, 4)

        # Jogador 1
        if self.impostor == 1:
            palavra_jogador1 = "VOCÊ É O IMPOSTOR"
        else:
            palavra_jogador1 = self.palavra_secreta

        # Jogador 2
        if self.impostor == 2:
            palavra_jogador2 = "VOCÊ É O IMPOSTOR"
        else:
            palavra_jogador2 = self.palavra_secreta

        # Jogador 3
        if self.impostor == 3:
            palavra_jogador3 = "VOCÊ É O IMPOSTOR"
        else:
            palavra_jogador3 = self.palavra_secreta

        # Jogador 4
        if self.impostor == 4:
            palavra_jogador4 = "VOCÊ É O IMPOSTOR"
        else:
            palavra_jogador4 = self.palavra_secreta

        # Mostrar palavras
        self.player1_word = ctk.CTkLabel(
            self,
            text=f"Jogador 1: {palavra_jogador1}"
        )
        self.player1_word.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.player2_word = ctk.CTkLabel(
            self,
            text=f"Jogador 2: {palavra_jogador2}"
        )
        self.player2_word.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        self.player3_word = ctk.CTkLabel(
            self,
            text=f"Jogador 3: {palavra_jogador3}"
        )
        self.player3_word.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.player4_word = ctk.CTkLabel(
            self,
            text=f"Jogador 4: {palavra_jogador4}"
        )
        self.player4_word.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # Votação
        self.voting_label = ctk.CTkLabel(
            self,
            text="Quem é o impostor?"
        )
        self.voting_label.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

        self.player1_vote = ctk.CTkButton(
            self,
            text="Jogador 1",
            command=lambda: self.vote(1)
        )
        self.player1_vote.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )

        self.player2_vote = ctk.CTkButton(
            self,
            text="Jogador 2",
            command=lambda: self.vote(2)
        )
        self.player2_vote.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        self.player3_vote = ctk.CTkButton(
            self,
            text="Jogador 3",
            command=lambda: self.vote(3)
        )
        self.player3_vote.grid(
            row=4,
            column=0,
            padx=10,
            pady=10
        )

        self.player4_vote = ctk.CTkButton(
            self,
            text="Jogador 4",
            command=lambda: self.vote(4)
        )
        self.player4_vote.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

    def vote(self, voted_player):

        if voted_player == self.impostor:

            self.voting_label.configure(
                text=f"Acertou! O Jogador {self.impostor} era o impostor!"
            )

        else:

            self.voting_label.configure(
                text=f"Errou! O Jogador {self.impostor} era o impostor!"
            )


app = Game()
app.mainloop()

