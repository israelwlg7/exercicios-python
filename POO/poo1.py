


class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise ValueError("Plano inválido. Escolha entre 'basic' ou 'premium'.")
    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"ver Filme {filme}")
        elif self.plano == "premium":
            print(f"ver Filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium para assistir a este filme")
        else:
            print("Plano inválido")


cliente = Cliente("Israel", "israel@gmail.com", "basic")
lista = [
    cliente.nome,
    cliente.email,
    cliente.plano,
    cliente.ver_filme("Vingadores", "premium")
]
print("-------------------------------------------------------")
print(f"\n O seu nome é {lista[0]}, seu email é {lista[1]} e seu plano é {lista[2]}")
print("-------------------------------------------------------")
cliente.mudar_plano("premium")

print(f"\n O seu nome é {lista[0]}, seu email é {lista[1]} e seu plano é {cliente.plano}")
