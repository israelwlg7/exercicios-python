class Advinhação:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def jogar(self):
        print("Bem-vindo ao jogo de adivinhação!")
        print("Tente adivinhar o número secreto entre 1 e 100.")

        while True:
            try:
                palpite = int(input("Digite seu palpite: "))
                if palpite < 1 or palpite > 100:
                    print("Por favor, digite um número entre 1 e 100.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
                continue

            if palpite < self.numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > self.numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número secreto: {self.numero_secreto}")
                break
if __name__ == "__main__":
    import random
    numero_secreto = random.randint(1, 100) 
    jogo = Advinhação(numero_secreto)
    jogo.jogar()